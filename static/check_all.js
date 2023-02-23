function tick_all(check) {
    let det_checks = document.getElementsByName(check.getAttribute("afecta"));
    for (let i = 0; i < det_checks.length; i++) {
        if (check.checked == true) {
            det_checks[i].value = 1;
        }
        else {
            det_checks[i].value = 0;
        }
    }
}