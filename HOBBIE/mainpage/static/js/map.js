$(window).load(function () {
    var svg = document.querySelector('object').getSVGDocument().documentElement;
    var paths = svg.getElementsByTagName("path");
    var i;
    for (i=0; i<paths.length;i++) {
        paths[i].addEventListener('click', addLink );
        $(paths[i]).mouseleave(HideTooltip);
        $(paths[i]).mouseenter(linkHover);
    }

    function linkHover() {
        var region_id = this.getAttribute('data-region');
        var links = document.getElementsByClassName('col-4 b-cities')[0].getElementsByTagName('a')
        for (i=0; i<links.length; i++) {
            if ($(links[i]).attr('id').indexOf(region_id) > -1) {
                $(links[i]).attr('data-state', 'hover');
            }
        }
    }

    function HideTooltip()
	{
        var tooltip = this.parentElement.getElementById('tooltip');
	    var tooltip_bg = this.parentElement.getElementById('tooltip_bg');
	    tooltip.setAttributeNS(null,"visibility","hidden");
	    tooltip_bg.setAttributeNS(null,"visibility","hidden");
        var region_id = this.getAttribute('data-region');
        var links = document.getElementsByClassName('col-4 b-cities')[0].getElementsByTagName('a')
        for (i=0; i<links.length; i++) {
            if ($(links[i]).attr('id').indexOf(region_id) > -1) {
                $(links[i]).attr('data-state', '');
            }
        }
	}

    function addLink(e) {
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
        }
    }
}