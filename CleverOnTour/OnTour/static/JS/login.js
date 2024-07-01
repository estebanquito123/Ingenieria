document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('loginForm');

    form.addEventListener('submit', function(event) {
        if (!validateForm()) {
            event.preventDefault();
        }
    });

    function validateForm() {
        let isValid = true;

        const username = document.getElementById('username');
        const password = document.getElementById('password');

        clearError(username);
        clearError(password);

        if (username.value.trim() === '') {
            showError(username, 'El nombre de usuario es obligatorio');
            isValid = false;
        }

        if (password.value.trim() === '') {
            showError(password, 'La contraseña es obligatoria');
            isValid = false;
        }

        return isValid;
    }

    function showError(element, message) {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        errorDiv.innerText = message;
        element.parentElement.appendChild(errorDiv);
    }

    function clearError(element) {
        const errorDiv = element.parentElement.querySelector('.error-message');
        if (errorDiv) {
            errorDiv.remove();
        }
    }
});