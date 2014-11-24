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
        {
            'toggle': $('#by_date').is(':checked'),
            'region': document.getElementById('region_select').selectedIndex,
            'p': 1,
            'view': getView(),
            'search_string': $('#search_string').val(),
            'category_name': document.URL.split('/')[document.URL.split('/').length - 2]
        });
}

function getSort() {
    if ($('#by_people').is(':checked')) {
        return 'by_people'
    }
    if ($('#by_date').is(':checked')) {
        return 'by_date'
    }
}


function ajaxView(view) {
    views = ['gallery_view', 'table_view', 'list_view'];
    Dajaxice.room.rooms_list(Dajax.process,
        {
            'toggle': getSort(),
            'region': document.getElementById('region_select').selectedIndex,
            'p': 1,
            'view': view,
            'search_string': $('#search_string').val(),
            'category_name': document.URL.split('/')[document.URL.split('/').length - 2]
        });
    $("label[for='" + view + "']").css('color', 'white');
    views.splice($.inArray(view, views), 1);
    $.each(views, function (i, val) {
        $("label[for='" + val + "']").css('color', 'inherit');
    });
}

function ajaxSort(sort) {
    sorts = ['by_people', 'by_date'];
    Dajaxice.room.rooms_list(Dajax.process,
        {
            'toggle': sort,
            'region': document.getElementById('region_select').selectedIndex,
            'p': 1,
            'view': getView(),
            'search_string': $('#search_string').val(),
            'category_name': document.URL.split('/')[document.URL.split('/').length - 2]
        });
    $("label[for='" + sort + "']").css('color', 'white');
    sorts.splice($.inArray(sort, sorts), 1);
    $.each(sorts, function (i, val) {
        $("label[for='" + val + "']").css('color', 'inherit');
    });
}
var invited_users = [];

function append(element) {
    atr = $(element).attr('for');
    input_ischecked = $("#" + atr).prop('checked');
    if (!input_ischecked) {
        invited_users.push($(element).attr('name'));
    } else {
        position = $.inArray($(element).attr('name'), invited_users);
        invited_users.splice(position, 1);
    }
}

function getSearch() {
    var $keywords = $(".tagsinput").children(".tag");
    var tags = [];
    for (var i = $keywords.length; i--;) {
        tags.push($($keywords[i]).text().substring(0, $($keywords[i]).text().length - 1).trim());
    }
    var uniqueTags = $.unique(tags);
    return uniqueTags.toString();/*.replace(",", " ")*/
}