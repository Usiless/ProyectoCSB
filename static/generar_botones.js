﻿$(document).ready(function () {
    var data = document.getElementById("botones_js").getAttribute("data");
    var actualizar = document.getElementById("botones_js").getAttribute("actualizar");
    var eliminar = document.getElementById("botones_js").getAttribute("eliminar");
    var element = document.getElementById("botones");
    var e = document.getElementsByClassName("form-control");
    var d = document.getElementsByClassName("deshab");

    if (data) {
        console.log("No está vacío");
        if (actualizar == 1) {
            agregar_editar();
            for (var i = 0; i < e.length; i++) {
                if (e[i].className != "form-control det") {
                    e[i].removeAttribute("disabled");
                }
            }
        }
        else {
            for (var i = 0; i < e.length; i++) {
                if (e[i].className != "form-control det") {
                    e[i].setAttribute('disabled', 'disabled');
                }
            }
        }
        if (eliminar == 1) {
            agregar_eliminar();
        }
        for (var i = 0; i < d.length; i++) {
            d[i].setAttribute('disabled', 'disabled');
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