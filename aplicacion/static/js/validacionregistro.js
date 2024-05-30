const formulasioregistro = document.getElementById            
// Obtener el formulario por su ID
const formularioregistro = document.getElementById('formularioregistro');

// Obtener los campos del formulario por su ID
const usuario = document.getElementById('usuario');
const correo = document.getElementById('correo')
const constraseña = document.getElementById('constraseña');

// Expresiones regulares de validación
const expresiones = {
    usuario: /^[a-zA-Z0-9_-]{3,16}$/,
    correo: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
    contraseña: /^(.){4,12}$/ // Entre 4 y 12 caracteres
}
//mensaje de validacion para cada campo
const mensajes = {
    usuario: 'Por favor ingresa un usuario válido.',
    correo: 'Por favor, ingrese un correo válido',
    contraseña: 'Por favor ingresa una contraseña válida.'
}

// Validar cada campo mientras se escribe
usuario.addEventListener('input', () => validarCampo(expresiones.usuario, usuario, mensajes.usuario));
correo.addEventListener('input', () => validarCampo(expresiones.correo, correo, mensajes.correo));
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
formularioregistro.addEventListener('submit', function(event) {
    event.preventDefault(); // Evitar el envío por defecto

    // Validar cada campo usando las expresiones regulares y las funciones de validación
    validarCampo(expresiones.usuario, usuario, mensajes.usuario);
    validarCampo(expresiones.correo, correo, mensajes.correo);
    validarCampo(expresiones.contraseña, contraseña, mensajes.contraseña);

    // Si todos los campos son válidos, enviar el formulario
    if (usuario.classList.contains('is-valid') && correo.classList.contains('is-valid') && contraseña.classList.contains('is-valid')) {
        this.submit();
    }
});