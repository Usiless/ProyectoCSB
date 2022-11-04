$(document).ready(function () {
    var data = document.getElementById("botones_js").getAttribute("data");
    var actualizar = document.getElementById("botones_js").getAttribute("actualizar");
    var eliminar = document.getElementById("botones_js").getAttribute("eliminar");
    var element = document.getElementById("botones");
    console.log(eliminar)
    console.log(actualizar)
    if (data) {
        console.log("No está vacío");
        if (eliminar == 1) {
            agregar_eliminar();
        }
        if (actualizar == 1) {
            agregar_editar();
        }
    }
    else {
        agregar_guardar();
        console.log("Está vacío");
    }
    agregar_cancelar();

    function agregar_eliminar() {
        let btn = document.createElement("button");
        btn.innerHTML = "Eliminar";
        btn.type = "submit";
        btn.value = "btn_delete";
        btn.name = "btn_submit";
        btn.className = "btn btn-danger";
        element.appendChild(btn);
    }

    function agregar_editar() {
        let btn = document.createElement("button");
        btn.innerHTML = "Editar";
        btn.type = "submit";
        btn.value = "btn_editar";
        btn.name = "btn_submit";
        btn.className = "btn btn-primary";
        element.appendChild(btn);
    }

    function agregar_guardar() {
        let btn = document.createElement("button");
        btn.innerHTML = "Guardar";
        btn.type = "submit";
        btn.name = "btnGuardar";
        btn.className = "btn btn-primary";
        element.appendChild(btn);
    }

    function agregar_cancelar() {
        let btn = document.createElement("a");
        btn.innerHTML = "Cancelar";
        btn.type = "input";
        btn.name = "btnCancelar";
        btn.className = "btn btn-danger";
        btn.setAttribute("onClick", "history.back()");
        element.appendChild(btn);
    }
})