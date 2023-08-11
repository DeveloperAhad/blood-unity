(function ($) {
    'use strict';
    $('#id_district').empty()
    $('#id_upazila').empty()
    $('#id_union').empty()
    $('#id_division').on('change', function (e) {
        $('#id_district').empty()
        $('#id_upazila').empty()
        $('#id_union').empty()
        $.ajax({
            url: '/locations/districts?division_id=' + $(this).val(),
        }).done(function (data) {
            $('#id_district').append('<option>---------</option>')
            data['districts'].forEach(function (district) {
                $('#id_district').append('<option value="' + district.id + '">' + district.name + '</option>')
            })
        })
    })

    $('#id_district').on('change', function (e) {
        $('#id_upazila').empty()
        $('#id_union').empty()
        $.ajax({
            url: '/locations/upazilas?district_id=' + $(this).val(),
        }).done(function (data) {
            $('#id_upazila').append('<option>---------</option>')
            data['upazilas'].forEach(function (upazila) {
                $('#id_upazila').append('<option value="' + upazila.id + '">' + upazila.name + '</option>')
            })
        })
    })

    $('#id_upazila').on('change', function (e) {
        $('#id_union').empty()
        $.ajax({
            url: '/locations/unions?upazila_id=' + $(this).val(),
        }).done(function (data) {
            $('#id_union').append('<option>---------</option>')
            data['unions'].forEach(function (union) {
                $('#id_union').append('<option value="' + union.id + '">' + union.name + '</option>')
            })
        })
    })


})(jQuery);