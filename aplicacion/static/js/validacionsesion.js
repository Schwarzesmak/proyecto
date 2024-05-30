const formulasiosesion = document.getElementById            
// Obtener el formulario por su ID
const formulariosesion = document.getElementById('formulariosesion');

// Obtener los campos del formulario por su ID
const usuario = document.getElementById('usuario');
const constraseña = document.getElementById('constraseña');

// Expresiones regulares de validación
const expresiones = {
    usuario: /^[a-zA-Z0-9_-]{3,16}$/,
    contraseña: /^(.){4,12}$/ // Entre 4 y 12 caracteres
}
//mensaje de validacion para cada campo
const mensajes = {
    usuario: 'Por favor ingresa un usuario válido.',
    contraseña: 'Por favor ingresa una contraseña válida.'
}

// Validar cada campo mientras se escribe
usuario.addEventListener('input', () => validarCampo(expresiones.usuario, usuario, mensajes.usuario));
contraseña.addEventListener('input', () => validarCampo(expresiones.contraseña, contraseña, mensajes.contraseña));

// Función para validar un campo
function validarCampo(expresion, input, mensaje) {
    if (expresion.test(input.value)) {
        // Campo válido
        input.classList.remove('is-invalid');
        input.classList.add('is-valid');
        // Eliminar mensaje de error si existe
        const error = input.nextElementSibling;
        if (error && error.classList.contains('invalid-feedback')) {
            error.remove();
        }
    } else {
        // Campo inválido
        input.classList.add('is-invalid');
        input.classList.remove('is-valid');
        // Mostrar mensaje de error
        const error = input.nextElementSibling;
        if (!error || !error.classList.contains('invalid-feedback')) {
            const divError = document.createElement('div');
            divError.classList.add('invalid-feedback');
            input.parentNode.appendChild(divError);
        }
        input.nextElementSibling.innerText = mensaje;
    }
}
// Validar cada campo del formulario al enviarlo
formulariosesion.addEventListener('submit', function(event) {
    event.preventDefault(); // Evitar el envío por defecto

    // Validar cada campo usando las expresiones regulares y las funciones de validación
    validarCampo(expresiones.usuario, usuario, mensajes.usuario);
    validarCampo(expresiones.contraseña, contraseña, mensajes.contraseña);

    // Si todos los campos son válidos, enviar el formulario
    if (usuario.classList.contains('is-valid') && contraseña.classList.contains('is-valid')) {
        this.submit();
    }
});