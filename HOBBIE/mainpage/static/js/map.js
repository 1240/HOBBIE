$(window).load(function () {
    var svg = document.querySelector('object').getSVGDocument().documentElement;
    var paths = svg.getElementsByTagName("path");
    var i;
    for (i=0; i<paths.length;i++) {
        paths[i].addEventListener('click', showAlert )
        $(paths[i]).mouseleave(HideTooltip)
    }

    function HideTooltip()
	{
        var tooltip = this.parentElement.getElementById('tooltip');
	    var tooltip_bg = this.parentElement.getElementById('tooltip_bg');
	    tooltip.setAttributeNS(null,"visibility","hidden");
	    tooltip_bg.setAttributeNS(null,"visibility","hidden");
	}

    function showAlert(e) {
        var title = this.getAttribute("data-title");
        var id = this.getAttribute("data-region");
        var a_now = document.getElementById("region_" + id);
        a_now.click();
    }
});


function addHover(region_id) {
    var svg = document.querySelector('object').getSVGDocument().documentElement;
    var paths = svg.getElementsByTagName("path");
    var i;
    for (i=0; i<paths.length;i++) {
        if (region_id.indexOf(paths[i].getAttribute('data-region')) > -1) {
            $(paths[i]).attr('data-state', 'hover');
            break;
        }
    }
}


function deleteHover(region_id) {
    var svg = document.querySelector('object').getSVGDocument().documentElement;
    var paths = svg.getElementsByTagName("path");
    var i;
    for (i=0; i<paths.length;i++) {
        if (region_id.indexOf(paths[i].getAttribute('data-region')) > -1) {
            $(paths[i]).attr('data-state', '');
            break;
        }
    }
}