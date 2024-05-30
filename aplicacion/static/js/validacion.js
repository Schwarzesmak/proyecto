const formulario = document.getElementById('formulario');

const primer_nombre = document.getElementById('primer_nombre');
const segundo_nombre = document.getElementById('segundo_nombre');
const apellido = document.getElementById('apellido');
const direccion = document.getElementById('direccion');
const correo = document.getElementById('correo');
const celular = document.getElementById('celular');
const adicional = document.getElementById('adicional');
const direccion2 = document.getElementById('direccion2');

const expresiones = {
    primer_nombre:/^[a-zA-ZÀ-ÿ\s]{3,40}$/, // Letras y espacios, pueden llevar acentos.
    segundo_nombre:/^[a-zA-ZÀ-ÿ\s]{3,40}$/, // Letras y espacios, pueden llevar acentos.
    apellido:/^[a-zA-ZÀ-ÿ\s]{3,40}$/, // Letras y espacios, pueden llevar acentos.
    direccion:/^[a-zA-Z0-9\s,'-]*$/,
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
    celular: /^\d{9}$/,
    adicional: /^[a-zA-Z0-9\s.,'()"-]*$/,
    direccion2:/^[a-zA-Z0-9\s,'-]*$/,
}

// Mensajes de validación para cada campo
const mensajes = {
    primer_nombre: 'El nombre debe tener entre 3 y 40 letras',
    segundo_nombre: 'El nombre debe tener entre 3 y 40 letras',
    apellido: 'El apellido debe tener entre 3 y 40 letras',
    direccion: 'La dirección permite letras mayúsculas y minúsculas, números, espacios, comas, apóstrofes y guiones',
    correo: 'El correo electrónico debe tener un formato válido, por ejemplo, ejemplo@dominio.com',
    celular: 'Número celular de acuerdo a Chile',
    adicional: 'Letras y espacios',
    direccion2: 'La dirección permite letras mayúsculas y minúsculas, números, espacios, comas, apóstrofes y guiones',
}

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

// Validar cada campo mientras se escribe
primer_nombre.addEventListener('input', () => validarCampo(expresiones.primer_nombre, primer_nombre, mensajes.primer_nombre));
segundo_nombre.addEventListener('input', () => validarCampo(expresiones.segundo_nombre, segundo_nombre, mensajes.segundo_nombre));
apellido.addEventListener('input',() => validarCampo(expresiones.apellido, apellido, mensajes.apellido));
direccion.addEventListener('input', () => validarCampo(expresiones.direccion, direccion, mensajes.direccion));
correo.addEventListener('input', () => validarCampo(expresiones.correo, correo, mensajes.correo));
celular.addEventListener('input', () => validarCampo(expresiones.celular, celular, mensajes.celular));
adicional.addEventListener('input', () => validarCampo(expresiones.adicional, adicional, mensajes.adicional));
direccion2.addEventListener('input', () => validarCampo(expresiones.direccion2, direccion2, mensajes.direccion2));

// Validar cada campo del formulario al enviarlo
formulario.addEventListener('submit', function(event) {
    event.preventDefault(); // Evitar el envío por defecto

    // Validar cada campo usando las expresiones regulares y las funciones de validación
    validarCampo(expresiones.primer_nombre, primer_nombre, mensajes.primer_nombre);
    validarCampo(expresiones.segundo_nombre, segundo_nombre, mensajes.segundo_nombre);
    validarCampo(expresiones.direccion, direccion, mensajes.direccion);
    validarCampo(expresiones.correo, correo, mensajes.correo);
    validarCampo(expresiones.celular, celular, mensajes.celular);
    validarCampo(expresiones.adicional, adicional, mensajes.adicional);
    validarCampo(expresiones.direccion2, direccion2, mensajes.direccion2);
    
    // Si todos los campos son válidos, enviar el formulario
    if (primer_nombre.classList.contains('is-valid') &&
        segundo_nombre.classList.contains('is-valid') &&
        direccion.classList.contains('is-valid') &&
        correo.classList.contains('is-valid') &&
        celular.classList.contains('is-valid') &&
        adicional.classList.contains('is-valid') &&
        direccion2.classList.contains('is-valid')) {
        this.submit();
    }
});


