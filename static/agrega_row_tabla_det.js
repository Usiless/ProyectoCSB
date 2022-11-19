$(document).ready(function () {
    var data = document.getElementById("agrega_row").getAttribute("data");
    var i = 1;
    if (data) {
        i = data.split("), (").length+1;
	}
    var l = i;


    $("#delete_row").click(function () {
        if (i > l) {
            $("#addr" + (i - 1)).html('');
            i--;
        }
    });
})

function nuevo_lin(id, id_tabla){
    // let id = tabla[0].id
    // console.log(tabla)
    // console.log(id)
    // b = i - 1;
    let inten = $('#'+id_tabla).find('tr').length-2;
    console.log($('#'+id_tabla).find('tr'))
    console.log(inten)
    console.log(id_tabla)
    if (inten-1>=id){
        id=inten
    }
    let i = id
    let b = i-1
    console.log(document.getElementById('addr' + b))
    $('#addr' + id).html($('#addr' + b).html()).find('td:first-child').html(id + 1);
    $('#'+id_tabla).append('<tr id="addr' + (id + 1) + '"></tr>');
    // i++;
}