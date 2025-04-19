# Spam Detection Web Application

This project is a Flask-based web application designed to detect spam in phone calls and text messages. It uses keyword matching and regex patterns to identify spam messages and simple rules to detect spam phone calls. The application stores detection results in a MySQL database and provides a user-friendly interface to interact with the system.

## Features

- Detect spam in text messages using predefined keywords and regex patterns.
- Detect spam phone calls based on phone number patterns.
- Use machine learning models for enhanced spam and fraud detection.
- Store detection results in a MySQL database.
- View the history of recent spam detection results for calls and messages.
- Simple and clean web interface with multiple pages: Home, About, Detect, History, and Result.

## Machine Learning Models

This project uses two machine learning models to improve detection accuracy:

- `spam_text_model.pkl`: A model trained to detect spam in text messages.
- `cdr_fraud_model.pkl`: A model trained to detect fraudulent calls based on call detail records (CDR).
- `tfidf_vectorizer.pkl`: A TF-IDF vectorizer used to transform text data for the spam detection model.

These models are loaded and used within the backend application to classify incoming messages and calls.

## Project Structure

- `backend/`: Contains the Flask application code, templates, static files, and database configuration.
  - `app.py`: Main Flask application with routes and spam detection logic.
  - `db_config.py`: Database connection setup.
  - `templates/`: HTML templates for rendering web pages.
  - `static/`: CSS and JavaScript files for styling and interactivity.
- `data/`: Contains database schema and sample data files.
- `models/`: Contains pre-trained models (if any).
- `notebooks/`: Jupyter notebooks used for data analysis or model training.

## Installation and Setup

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set up a Python virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required Python packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the MySQL database:**

   - Create a MySQL database named `spam_detection`.
   - Run the SQL script `data/spam_detection.sql` to create necessary tables.

5. **Configure database connection:**

   - Update the `backend/db_config.py` file with your MySQL database credentials.

6. **Run the Flask application:**

   ```bash
   python backend/app.py
   ```

7. **Access the application:**

   Open your web browser and go to `http://127.0.0.1:5000/`

## Usage

- Use the **Home** page to navigate the application.
- Go to the **Detect** page to input a phone number or text message for spam detection.
- View the **History** page to see the last 10 spam detection results for calls and messages.
- Learn more about the project on the **About** page.

## Technologies Used

- Python 3
- Flask web framework
- MySQL database
- HTML, CSS, JavaScript for frontend
- Regex for spam detection logic

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.

## Contact

For any questions or feedback, please contact Niti Agnihotri at agnihotriniti28@gmail.com.
