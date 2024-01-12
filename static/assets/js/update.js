(function ($) {
    'use strict';


    var district_label = $('#id_district option:selected').text()
    var district_value = $('#id_district').val()
    var upazila_label = $('#id_upazila option:selected').text()
    var upazila_value = $('#id_upazila').val()
    var union_label = $('#id_union option:selected').text()
    var union_value = $('#id_union').val()

    $('#id_district').empty()
    $('#id_upazila').empty()
    $('#id_union').empty()

    $('#id_district').append('<option value="' + district_value + '">' + district_label + '</option>')
    $('#id_upazila').append('<option value="' + upazila_value + '">' + upazila_label + '</option>')
    $('#id_union').append('<option value="' + union_value + '">' + union_label + '</option>')




    $('#id_division').on('change', function (e) {
        $('#id_district').empty()
        $('#id_upazila').empty()
        $('#id_union').empty()

        $.ajax({
            url: '/locations/districts?division_id=' + $(this).val(),
        }).done(function (data) {
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