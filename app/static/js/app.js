console.log("öla")


$(document).ready(function() {
  // define as opções do segundo select
  var options = {
    'Código Penal': ['Ameaça', 'Infanticídio', 'Lesão Corporal', 'Lesão Grave', 'Lesão Gravíssima', 'Homicídio simples',
    'Homicídio qualificado', 'Feminicídio', 'Homicídio culposo',
    'Induzimento, instigação ou auxílio a suicídio ou a automutilação', 'Rixa', 'Calunia',
    'Difamação', 'Injúria', 'Abandono de incapaz', 'Abandono de incapaz com resultado de lesão grave',
    'Abandono de incapaz  com resultado morte']
,
    'Lei Maria da Penha': ['Desobediência', 'B.2', 'B.3'],
    'Lei de Drogas': ['Posse', 'Internacional', 'C.3'],
    'Lei 9.099/95': ['D.1', 'D.2', 'D.3'],
    'Lei de Lavagem': ['E.1', 'E.2', 'E.3'],
  };

  // define o manipulador de eventos para o primeiro select
  $('#legislacao').on('change', function() {
    // obtém a opção selecionada no primeiro select
    var selected = $(this).val();
    // obtém o segundo select
    var select = $('#crime');
    // remove todas as opções do segundo select
    select.empty();
    // adiciona as opções relevantes do objeto options com base na seleção do usuário
    if (selected in options) {
      for (var i = 0; i < options[selected].length; i++) {
        var option = $('<option>').val(options[selected][i]).text(options[selected][i]);
        select.append(option);
      }
    }
    // adiciona uma opção padrão
    select.prepend($('<option>').val('').text('Tipo Penal'));
  });
});


function show_hide_display()
{
  if (document.getElementById('suspensao_prescricao_true').checked)
      {
          document.getElementById('display_oculta').style.display='block'

      }
  if (document.getElementById('suspensao_prescricao_false').checked)
      {
          document.getElementById('display_oculta').style.display='none'
          document.getElementById('Dt_inicio_suspensao').value=''
          document.getElementById('Dt_fim_suspensao').value=''

      }

}

function show_hide_display_denuncia()
{
  if (document.getElementById('recebimento_denuncia_true').checked)
      {
          document.getElementById('display_oculta_denuncia').style.display='block'
      }

  if (document.getElementById('recebimento_denuncia_false').checked)
      {
          document.getElementById('display_oculta_denuncia').style.display='none'
          document.getElementById('Dt_Denuncia').value=''
      }
}


  const date1Input = document.querySelector('#Dt_inicio_suspensao');
  const date2Input = document.querySelector('#Dt_fim_suspensao');

  date2Input.addEventListener('change', function() {
    var date1 = new Date(date1Input.value);
    var date2 = new Date(date2Input.value);

    if (date2 < date1) {
      alert('A data final deve ser posterior à data inicial.');
      date2Input.value = '';
    }
  });





  const data_fato = document.querySelector('#formFileSm');
  const data_denuncia = document.querySelector('#Dt_Denuncia');

 data_denuncia.addEventListener('change', function() {
    var date1 = new Date(data_fato.value);
    var date2 = new Date(data_denuncia.value);

    if (date2 < date1) {
      alert('A data da Denúncia deve ser posterior à data do fato.');
      date2Input.value = '';
    }
  });



