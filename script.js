document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("form").forEach(form => {
        form.addEventListener("submit", function (event) {
            event.preventDefault(); // Prevent default form submission
            
            if (form.querySelector(".loading")) return; // Prevent duplicate loading messages
            
            let loading = document.createElement("p");
            loading.innerText = "Checking...";
            loading.className = "loading";
            form.appendChild(loading);

            const formData = new FormData(form);
            fetch(form.action, {
                method: form.method,
                body: formData
            })
            .then(response => response.text())
            .then(data => {
                loading.remove();
                const resultContainer = document.createElement("div");
                resultContainer.innerHTML = data;
                form.appendChild(resultContainer);
            })
            .catch(error => {
                loading.remove();
                console.error('Error:', error);
            });
        });
    });
});
