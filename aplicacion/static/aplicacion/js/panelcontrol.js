// Código para el gráfico de ventas
document.addEventListener("DOMContentLoaded", function() {
    var datos = {
        labels: ['Armas', 'Ropa', 'Otros'],
        datasets: [{
            label: 'NÚMERO DE VENTAS',
            backgroundColor: 'rgba(236, 33, 0, 0.8)', // Color del área
            borderColor: 'rgba(0, 0, 0, 1)', // Color de la línea
            borderWidth: 3,
            data: [28, 12, 23] // Datos de ventas por mes
        }]
    };

    var opciones = {
        responsive: true,
        maintainAspectRatio: false
    };
    var contexto = document.getElementById('miGrafico').getContext('2d');
    new Chart(contexto, {
        type: 'bar', // Tipo de gráfico (puedes cambiarlo a 'bar', 'pie', etc.)
        data: datos,
        options: opciones
    });
});

// Código para la fecha y la API de Unix Time
$(document).ready(function () {
    var currentDateTime = new Date();
    var formattedDateTime = currentDateTime.toLocaleString('es-ES');
    $("#currentDateTime").text(formattedDateTime);

    $.getJSON('https://digidates.de/api/v1/unixtime', function (data) {
        console.log("Datos recibidos:", data);
        $("#unixTimeText").text("Unix time actual: " + data.time);
    }).fail(function () {
        console.log("Error al cargar los datos del API de digidates.");
        $("#unixTimeText").text("Error al cargar los datos");
    });
});

// Código para la API del clima
const apiKey = 'cc45799586736f73cd1770474d4d58ca';
const city = 'Concepcion'; // Cambia la ciudad según tu ubicación

// Construir la URL de la solicitud
const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&lang=es&units=metric`;

// Realizar la solicitud a la API
fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
        console.log(data);

        // Extraer los datos necesarios
        const temperatura = data.main.temp;
        const descripcion = data.weather[0].description;

        // Mostrar los datos en el documento HTML
        const weatherData = document.getElementById('weatherData');
        weatherData.innerHTML = `<p>Temperatura: ${temperatura}°C</p>
                                 <p>Descripción: ${descripcion}</p>`;
    })
    .catch(error => {
        console.log('Error al obtener los datos del clima:', error);
        const weatherData = document.getElementById('weatherData');
        weatherData.innerHTML = '<p>Ocurrió un error al cargar los datos del clima</p>';
    });
