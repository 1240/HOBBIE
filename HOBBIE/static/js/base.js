/**
 * Created by 1240 on 30.10.2014.
 */

$(document).ready(function () {
    $(".left-off-canvas-toggle")[0].addEventListener('click', leftSlide);
    $(".right-off-canvas-toggle")[0].addEventListener('click', rightSlide);
    $(".exit-off-canvas")[0].addEventListener('click', exitCanvas);

});

function exitCanvas(e) {
    var main_div = $(".off-canvas-wrap");
    main_div.attr('class', "off-canvas-wrap");
}

function leftSlide(e) {
    var main_div = $(".off-canvas-wrap");
    main_div.addClass("move-right");
}

function rightSlide(e) {
    var main_div = $(".off-canvas-wrap");
    main_div.addClass("move-left");
}
