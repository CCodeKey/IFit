document.addEventListener("DOMContentLoaded", function () {
    const contactButton = document.getElementById("contactButton");
    
    if (contactButton) {
        contactButton.addEventListener("click", function (event) {
            event.preventDefault();
            alert("Obrigado por entrar em contato! Responderemos em breve.");
            
            const contactSection = contactButton.closest(".section");
            if (contactSection) {
                contactSection.scrollIntoView({ behavior: "smooth" });
            }
        });
    }
});