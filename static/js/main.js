
function calculate_price(object_select, object_price, prices) {

    var selectElement = document.getElementById(object_select);
    var selectedColor = selectElement.value;

    
    if (selectedColor == 'option1') {
        selectedColor = 0;
    }
    else if (selectedColor == 'option2') {
        selectedColor = 1;
    }
    else if (selectedColor == 'option3') {
        selectedColor = 2;
    }
    else {
        selectedColor = 0;
    }

    var price_x = document.getElementById(object_price);
    price_x.innerText = prices[selectedColor] + '€';
}

function show_info(titulo, descripcion) {
    Swal.fire({
    title: `<strong>${titulo}</strong>`,
    icon: "success",
    html: `
        <code>${descripcion}</code>
    `,
    showCloseButton: true,
    showCancelButton: true,
    focusConfirm: false,
    confirmButtonText: `
        <i class="fa fa-thumbs-up"></i> Great!
    `,
    confirmButtonAriaLabel: "Thumbs up, great!",
    cancelButtonText: `
        <i class="fa fa-thumbs-down"></i>
    `,
    cancelButtonAriaLabel: "Thumbs down"
    });
}

function updatePrice() {
    var priceSelector = document.getElementById("precio-seleccionado".value);
    var priceOption = document.getElementById("price-option".value);

    // Obtener el valor seleccionado
    //	var selectedOption = precio-seleccionado.value;
    let selectedOption = document.getElementById(precio-seleccionado.value)

    // Actualizar el texto según el valor seleccionado
    switch (selectedOption) {
        case "option1":
            priceOption.textContent = "$3.95";
            break;
        case "option2":
            priceOption.textContent = "$10.95";
            break;
        case "option3":
            priceOption.textContent = "$17.95";
            break;
        default:
            priceOption.textContent = "Selecciona un precio";
            break;
    }
}
                                                            
function actualizarContador() {
    // Establece la fecha objetivo (puede ser en el futuro)
    let fechaInicio = new Date("2021-03-01T00:00:00");
    let fechaObjetivo = new Date("2023-07-17T23:59:59");
    let ahora = new Date();
    let tiempoTranscurrido = ahora - fechaInicio;

    // Calcula los días, horas, minutos y segundos transcurridos
    let dias = Math.floor(tiempoTranscurrido / (1000 * 60 * 60 * 24));
    let horas = Math.floor((tiempoTranscurrido % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    let minutos = Math.floor((tiempoTranscurrido % (1000 * 60 * 60)) / (1000 * 60));
    let segundos = Math.floor((tiempoTranscurrido % (1000 * 60)) / 1000);

    // Actualiza los elementos HTML con los valores del contador
    document.getElementById("dias").textContent = dias.toString().padStart(2, "0");
    document.getElementById("horas").textContent = horas.toString().padStart(2, "0");
    document.getElementById("minutos").textContent = minutos.toString().padStart(2, "0");
    document.getElementById("segundos").textContent = segundos.toString().padStart(2, "0");
}

// Actualiza el contador cada segundo
setInterval(actualizarContador, 1000);


// JS CALCU EC

function calcularEc() {
    semanaCultivo = document.getElementById("semanaCultivoCliente").value;
    ecAguaRiego = document.getElementById("ecAguaRiegoCliente").value;
    litrosUsados = document.getElementById("litrosUsadosCliente").value;

    let m1 = "Añada más comida base al agua para subir la ec.";
    let m2 = "Su ec está perfecta.";
    let m3 = ("Añada " + (0.2 * litrosUsados) + " litros de agua de ósmosis para bajar su ec.");

    // m1 si esta baja, m2 perfect y m3 mas alta

    //semana 1
    if (semanaCultivo === 1 && ecAguaRiego < 0.5) {
        console.log(m1);
    } else if (semanaCultivo === 1 && ecAguaRiego >= 0.5 && ecAguaRiego <= 0.7) {
        console.log(m2);
    } else if (semanaCultivo === 1 && ecAguaRiego > 0.7) {
        console.log(m3);
        //semana 2, 3 y 4
    } else if ([2, 3, 4].includes(semanaCultivo) && ecAguaRiego < 0.6) {
        console.log(m1);
    } else if ([2, 3, 4].includes(semanaCultivo) && ecAguaRiego >= 0.6 && ecAguaRiego <= 0.8) {
        console.log(m2);
    } else if ([2, 3, 4].includes(semanaCultivo) && ecAguaRiego > 0.8) {
        console.log(m3);
        //semana 5
    } else if (semanaCultivo === 5 && ecAguaRiego < 1) {
        console.log(m1);
    } else if (semanaCultivo === 5 && ecAguaRiego >= 1 && ecAguaRiego <= 1.2) {
        console.log(m2);
    } else if (semanaCultivo === 5 && ecAguaRiego > 1.2) {
        console.log(m3);
        //semana 6
    } else if (semanaCultivo === 6 && ecAguaRiego < 1.2) {
        console.log(m1);
    } else if (semanaCultivo === 6 && ecAguaRiego >= 1.2 && ecAguaRiego <= 1.4) {
        console.log(m2);
    } else if (semanaCultivo === 6 && ecAguaRiego > 1.4) {
        console.log(m3);
        //semana 7
    } else if (semanaCultivo === 7 && ecAguaRiego < 1.4) {
        console.log(m1);
    } else if (semanaCultivo === 7 && ecAguaRiego >= 1.4 && ecAguaRiego <= 1.6) {
        console.log(m2);
    } else if (semanaCultivo === 7 && ecAguaRiego > 1.6) {
        console.log(m3);
        //semana 8
    } else if (semanaCultivo === 8 && ecAguaRiego < 1.6) {
        console.log(m1);
    } else if (semanaCultivo === 8 && ecAguaRiego >= 1.6 && ecAguaRiego <= 1.8) {
        console.log(m2);
    } else if (semanaCultivo === 8 && ecAguaRiego > 1.8) {
        console.log(m3);
        //semana 9 y 10
    } else if ((semanaCultivo === 9 || 10) && ecAguaRiego < 1.8) {
        console.log(m1);
    } else if ((semanaCultivo === 9 || 10) && ecAguaRiego >= 1.8 && ecAguaRiego <= 2) {
        console.log(m2);
    } else if ((semanaCultivo === 9 || 10) && ecAguaRiego > 1.8) {
        console.log(m3);
        //semana 11 
    } else if (semanaCultivo === 11 && ecAguaRiego < 1.5) {
        console.log(m1);
    } else if (semanaCultivo === 11 && (ecAguaRiego >= 1.5 && ecAguaRiego <= 1.6)) {
        console.log(m2);
    } else if (semanaCultivo === 11 && ecAguaRiego > 1.6) {
        console.log(m3);
        //semana 12
    } else if (semanaCultivo === 12 && ecAguaRiego < 1.2) {
        console.log(m1);
    } else if (semanaCultivo === 12 && (ecAguaRiego >= 1.2 && ecAguaRiego <= 1.3)) {
        console.log(m2);
    } else if (semanaCultivo === 12 && ecAguaRiego > 1.3) {
        console.log(m3);
    }
}