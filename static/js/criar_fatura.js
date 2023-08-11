
function updateValorFinal() {
  let valor_final =
    $('#id_valor').val() - ($('#id_desconto').val() / 100) * $('#id_valor').val()
  $('#valor_final').text(
    valor_final.toLocaleString('pt-br', {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2,
    })
  )
}

$(document).ready(function () {
  
  var $cnpj = $('input[name=cnpj]')
  $cnpj.mask('00.000.000/0000-00', { reverse: true })

  $('input[name=cnpj]').blur(function () {
    var cnpj = $(this).val()

    function limpa_formulário() {
      // Limpa valores do formulário de cep.
      $('#empresa').val('')
      $('#valor').val('')
      $('#inscricao').val('')
    }

    if (cnpj) {
      $('#empresa').val('...')
      $('#valor').val('...')
      $('#inscricao').val('...')

      var url = '/admin/consulta-cnpj/?cnpj=' + cnpj
      $.getJSON(url, function (json) {
        for (item in json) {
          console.log(item)
        }
        debugger;
      
          const fatura = json[0]
          let total = 0
          json.forEach((item) => {
            total += parseFloat(
              fatura.valorTotalConsolidadoMoeda
                .replaceAll('.', '')
                .replaceAll(',', '.')
            )
          })
          $('#id_empresa').val(fatura.nomeDevedor)
          $('#id_valor').val(total.toFixed(2))
          $('#id_inscricao').val(fatura.numeroInscricao)
          $('#id_nomeUnidade').val(fatura.nomeUnidade)
          $('#id_email').val(fatura.email)
          $('#id_porcetagem').val(fatura.percentage)
          $('#id_numero_parcelas').val(fatura.numero_parcelas)
          $('#id_valor_entrada').val(fatura.entrada)
          
       
      })
    }

    updateValorFinal()
  })
})

updateValorFinal()

$('#id_desconto').on('input', function () {
  updateValorFinal()
})

$('#id_valor').on('input', function () {
  updateValorFinal()
})


