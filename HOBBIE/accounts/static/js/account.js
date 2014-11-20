/**
 * Created by 1240 on 20.11.2014.
 */

function sex_choice(sort) {
    sorts = ['id_man', 'id_woman'];
    $("label[for='" + sort + "']").css('color', 'white');
    sorts.splice($.inArray(sort, sorts), 1);
    $.each(sorts, function (i, val) {
        $("label[for='" + val + "']").css('color', 'inherit');
    });
    if (sort == 'id_man') {
        $("#id_sex").prop('checked', true)
    } else {
        $("#id_sex").prop('checked', false)
    }
}