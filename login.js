document.addEventListener("DOMContentLoaded", function() {
    const loginForm = document.getElementById("loginForm");
    const errorMessage = document.getElementById("errorMessage");

    loginForm.addEventListener("submit", function(event) {
        event.preventDefault();

        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        if (username === "" || password === "") {
            errorMessage.textContent = "Por favor, preencha todos os campos.";
        } else if (username === "usuario" && password === "senha123") {
            alert("Login bem-sucedido!");

        } else {
            errorMessage.textContent = "Usuário ou senha incorretos.";
        }
    });
});