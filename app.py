from flask import Flask, render_template, request
from db_config import get_db_connection
import re  # For regex-based spam detection

app = Flask(__name__)

# Spam detection logic
SPAM_KEYWORDS = [
    "win cash", "urgent action", "click here", "lottery", "reset password", "free money",
    "bank account blocked", "claim now", "limited offer", "verify now", "lucky winner",
    "congratulations", "selected for", "100% free", "work from home", "betting", "earn ₹",
    "credit card offer", "act fast", "double your money", "scam", "fake", "urgent",
    "you have won", "prize", "cashback", "invest now", "hurry", "reward",
    "exclusive deal", "limited time offer", "act now", "urgent response needed", "risk-free"
]

SPAM_PATTERNS = [
    r"free\s+\w+",  # Free something
    r"claim\s+now",  # Claim now!
    r"click\s+(here|below)",  # Click here/below
    r"\$\d+",  # Money amounts like "$1000"
    r"\d{10}",  # 10-digit number (common in scam calls)
    r"(account|password).*reset",  # Reset password/account
    r"congrats|winner|you\s+won",  # Lottery scams
    r"urgent|immediate\s+action",  # Urgent action required!
    r"betting|invest\s+now",  # Investment scams
]

def detect_spam(message):
    """Detects spam based on keywords and regex patterns."""
    message = message.lower()
    if any(keyword in message for keyword in SPAM_KEYWORDS):
        return "Spam", 0.97
    for pattern in SPAM_PATTERNS:
        if re.search(pattern, message):
            return "Spam", 0.95
    return "Not Spam", 0.99

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/detect", methods=["GET", "POST"])
def detect():
    if request.method == "POST":
        return render_template("detect.html")
    return render_template("detect.html")

@app.route("/history")
def history():
    """Retrieve the last 10 records of call and message history."""
    conn = get_db_connection()
    call_history, message_history = [], []

    if conn:
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM spam_calls ORDER BY timestamp DESC LIMIT 10")
            call_history = cursor.fetchall()

            cursor.execute("SELECT * FROM spam_messages ORDER BY timestamp DESC LIMIT 10")
            message_history = cursor.fetchall()
        finally:
            cursor.close()
            conn.close()

    return render_template("history.html", call_history=call_history, message_history=message_history)

@app.route("/detect_call", methods=["POST"])
def detect_call():
    phone_number = request.form["phone"]

    if not re.match(r"^[6789]\d{9}$", phone_number):
        result, confidence = "Invalid", 0.0
    elif phone_number.startswith("999"):
        result, confidence = "Spam", 0.98
    else:
        result, confidence = "Not Spam", 0.99

    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO spam_calls (phone_number, prediction, confidence) VALUES (%s, %s, %s)", 
                           (phone_number, result, confidence))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    return render_template("result.html", 
                           message=f"Phone Number: {phone_number} - {result} ({int(confidence * 100)}% confidence)", 
                           result=result, confidence=confidence)

@app.route("/detect_text", methods=["POST"])
def detect_text():
    message = request.form["message"]
    result, confidence = detect_spam(message)

    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO spam_messages (message, prediction, confidence) VALUES (%s, %s, %s)", 
                           (message, result, confidence))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    return render_template("result.html", 
                           message=f"Message: {message} - {result} ({int(confidence * 100)}% confidence)", 
                           result=result, confidence=confidence)

if __name__ == "__main__":
    app.run(debug=True)
