$(document).ready(function () {

    $(document).ready(function () {
        var $cnpj = $('input[name=cnpj]')
        $cnpj.mask('00.000.000/0000-00', { reverse: true })
        var $username = $('input[name=username]')
        $username.mask('00.000.000/0000-00', { reverse: true })
        $('#example').DataTable();
    });    
});
