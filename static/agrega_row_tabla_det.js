$(document).ready(function () {
    var data = document.getElementById("agrega_row").getAttribute("data");
    var i = 1;
    if (data) {
        i = data.split("), (").length+1;
	}
    var l = i;
    $("#add_row").click(function () {
        b = i - 1;
        $('#addr' + i).html($('#addr' + b).html()).find('td:first-child').html(i + 1);
        $('#tab_logic').append('<tr id="addr' + (i + 1) + '"</tr>');
        i++;
    });
    $("#delete_row").click(function () {
        if (i > l) {
            $("#addr" + (i - 1)).html('');
            i--;
        }
    });
})