/**
 * Created by 1240 on 01.11.2014.
 */
function getView() {
    if ($('#gallery_view').is(':checked')) {
        return 'gallery_view'
    }
    if ($('#table_view').is(':checked')) {
        return 'table_view'
    }
    if ($('#list_view').is(':checked')) {
        return 'list_view'
    }
}

function roomsSort() {
    Dajaxice.accounts.rooms_list(Dajax.process,
        {'toggle': $('#by_date').is(':checked'),
            'p': 1,
            'view': getView()});
}

function getSort() {
    if ($('#by_people').is(':checked')) {
        return 'by_people'
    }
    if ($('#by_date').is(':checked')) {
        return 'by_date'
    }
}

$(document).ready(function () {
    $('#id_room_to_date').fdatetimepicker({
        format: 'mm-dd-yyyy hh:ii'
    });
});

function ajaxView(view) {
    views = ['gallery_view', 'table_view', 'list_view'];
    Dajaxice.accounts.rooms_list(Dajax.process,
        {'toggle': getSort(),
            'p': 1,
            'view': view});
    $("label[for='" + view + "']").css('color', 'white');
    views.splice( $.inArray(view, views), 1 );
    $.each(views, function(i, val ) {
      $("label[for='" + val + "']").css('color', 'inherit');
    });
}

function ajaxSort(sort) {
    sorts = ['by_people', 'by_date'];
    Dajaxice.accounts.rooms_list(Dajax.process,
        {'toggle': sort,
            'p': 1,
            'view': getView()});
    $("label[for='" + sort + "']").css('color', 'white');
    sorts.splice( $.inArray(sort, sorts), 1 );
    $.each(sorts, function(i, val ) {
      $("label[for='" + val + "']").css('color', 'inherit');
    });
}