document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('registroForm');
    
    form.addEventListener('submit', function(event) {
        // Evitar el envío del formulario si hay errores de validación
        if (!validateForm()) {
            event.preventDefault();
        }
    });

    function validateForm() {
        let isValid = true;

        // Validar nombre de usuario
        const username = document.getElementById('id_username');
        if (username.value.trim() === '') {
            showError(username, 'El nombre de usuario es obligatorio');
            isValid = false;
        } else {
            clearError(username);
        }

        // Validar nombre
        const firstName = document.getElementById('id_first_name');
        if (firstName.value.trim() === '') {
            showError(firstName, 'El nombre es obligatorio');
            isValid = false;
        } else {
            clearError(firstName);
        }

        // Validar apellido
        const lastName = document.getElementById('id_last_name');
        if (lastName.value.trim() === '') {
            showError(lastName, 'El apellido es obligatorio');
            isValid = false;
        } else {
            clearError(lastName);
        }

        // Validar correo electrónico
        const email = document.getElementById('id_email');
        if (email.value.trim() === '') {
            showError(email, 'El correo electrónico es obligatorio');
            isValid = false;
        } else if (!validateEmail(email.value.trim())) {
            showError(email, 'El correo electrónico no es válido');
            isValid = false;
        } else {
            clearError(email);
        }

        // Validar dirección
        const direccion = document.getElementById('id_direccion');
        if (direccion.value.trim() === '') {
            showError(direccion, 'La dirección es obligatoria');
            isValid = false;
        } else {
            clearError(direccion);
        }

        // Validar celular
        const celular = document.getElementById('id_celular');
                if (celular.value.trim() === '') {
                    showError(celular, 'El celular es obligatorio');
                    isValid = false;
                } else if (!validatePhone(celular.value.trim())) {
                    showError(celular, 'El celular debe contener solo números y tener una longitud de entre 10 y 15 caracteres');
                    isValid = false;
                } else {
                    clearError(celular);
                }

        // Validar contraseñas
        const password1 = document.getElementById('id_password1');
        const password2 = document.getElementById('id_password2');
        if (password1.value.trim() === '') {
            showError(password1, 'La contraseña es obligatoria');
            isValid = false;
        } else {
            clearError(password1);
        }

        if (password2.value.trim() === '') {
            showError(password2, 'Confirmar la contraseña es obligatorio');
            isValid = false;
        } else if (password1.value.trim() !== password2.value.trim()) {
            showError(password2, 'Las contraseñas no coinciden');
            isValid = false;
        } else {
            clearError(password2);
        }

        return isValid;
    }

    function showError(element, message) {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        errorDiv.innerText = message;
        element.parentElement.appendChild(errorDiv);
        element.classList.add('input-error');
    }

    function clearError(element) {
        const errorDiv = element.parentElement.querySelector('.error-message');
        if (errorDiv) {
            errorDiv.remove();
        }
        element.classList.remove('input-error');
    }

    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    function validatePhone(phone) {
        const re = /^[0-9]{9,15}$/;
        return re.test(phone);
    }
});