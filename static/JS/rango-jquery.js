$(document).ready(function() {
    $("#about-btn").click( function(event) {
        alert("You clicked the button using JQuery!");
        });
    });

$("p").hover( function() {
    $(this).css('color', 'red');
    },
    function() {
    $(this).css('color', 'blue');
    });

$("#about-btn").click( function(event) {
    msgstr = $("#msg").html()
    msgstr = msgstr + "ooo"
    $("#msg").html(msgstr)
    });

$('.rango-add').click(function () {
    var catid = $(this).attr("data-catid");
    var url = $(this).attr("data-url");
    var titile = $(this).attr("data-title");
    var me = $(this)
    $.get('/rango/add/',
        { category_id: catid, url: url, titile: titile }, function (data) {
            $('#pages').html(data);
            me.hide();
        });
});