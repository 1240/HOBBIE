/**
 * Created by 1240 on 28.10.2014.
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
    Dajaxice.room.rooms_list(Dajax.process,
        {'toggle': $('#by_date').is(':checked'),
            'region': document.getElementById('region_select').selectedIndex,
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
