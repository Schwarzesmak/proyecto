$(document).ready(function () {
    $("#spin").show();
    $("#spintext").show();
    
    $("#spinuf").show();
    $("#spintextuf").show();
    
    $.getJSON('https://mindicador.cl/api', function (data) {
        console.log("Datos recibidos:", data);
        $("#dolar").text("Valor dolar: $" + data.dolar.valor);
        $("#spin").hide();
        $("#spintext").hide();
    }).fail(function () {
        console.log("Error al cargar los datos de la API del dólar.");
        $("#spin").hide();
        $("#spintext").hide(); 
        $("#dolar").removeClass("h5");
        $("#dolar").css("font-size", "10px");
        $("#dolar").text("Error al cargar datos");
    });
    setTimeout(function () {
        $.getJSON('https://mindicador.cl/api', function (data) {
            console.log("Datos recibidos:", data);
            $("#uf").text("Valor UF: $" + data.uf.valor);
            $("#spinuf").hide();
            $("#spintextuf").hide();
        }).fail(function () {
            console.log("Error al cargar los datos de la API de la UF.");
            $("#spinuf").hide();
            $("#spintextuf").hide();
            $("#uf").removeClass("h5");
            $("#uf").css("font-size", "10px");
            $("#uf").text("Error al cargar datos");
        });
    }, 3000);
});

//ESTE ES EL API NUMERO 3 QUE QUEREMOS OCUPAR
$(document).ready(function () {
    $.getJSON('https://digidates.de/api/v1/unixtime', function (data) {
        console.log("Datos recibidos:", data);
        var tiempoLocal = new Date(data.time * 1000); // Multiplica por 1000 para convertir segundos a milisegundos
        var tiempoLocalString = tiempoLocal.toLocaleString(); // Obtiene la representación de hora local
        $("#cuadro3").text("Tiempo actual en hora local: " + tiempoLocalString);
    }).fail(function () {
        console.log("Error al cargar los datos del tiempo.");
        $("#cuadro3").text("Error al cargar los datos del tiempo.");
    });
});

