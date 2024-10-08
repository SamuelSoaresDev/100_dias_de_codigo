setInterval(atualizarRelogio,1000);

function atualizarRelogio() {
    var data = new Date();
    var horas = data.getHours();
    var minutos = data.getMinutes();
    var segundos = data.getSeconds();
    var dia = data.getDate();
    var mes = data.getMonth();
    var ano = data.getFullYear();

    if (horas < 10) {
        horas = "0" + horas;
    }
    if (minutos < 10) {
        minutos = "0" + minutos;
    }
    if (segundos < 10) {
        segundos = "0" + segundos;
    }
    if (dia < 10)
    {
        dia = "0" + dia;
    }
    if (mes < 10)
        {
            mes = "0" + mes;
        }

    var relogioDigital = horas + ":" + minutos + ":" + segundos;
    var dataDigital = dia + ":" + mes + ":" + ano;
    
    document.getElementById("clock").innerHTML = relogioDigital + " / " + dataDigital;
   
}

