// Função para carregar data selecionada no calendario sem precisar clicar no botão.

function submitIfFormComplete()
{
  // Check the select has something selected
  if (document.getElementById('selectOne').selectedIndex != '')
  {
      //document.getElementById('formID').submit();
  }
}

// Função pega apenas o dia selecionado no html e se for igual não carrega a função.
var dia_selecionado = (document.getElementById('selecionar_data').value).substr(-2);
function checkAndSubmit(){
  if ((document.getElementById('selecionar_data').value).substr(-2) != dia_selecionado){
      document.getElementById('formulario_data').submit();
      // alert((document.getElementById('selecionar_data').value).substr(-2))
  }
}


//-----------------------------------------//


// var mes_ano = document.getElementById('selecionar_mes').value;
//alert(mes_ano)

// var ano = new Date().getFullYear(); // ano atual
// var hoje = new Date().getDate();  // dia atual
// alert(hoje)
// document.getElementById("selecionar_data").setAttribute("value", mes_ano + "-" + hoje);
//document.getElementById('selecionar_data').setAttribute("max", ano + "-12-12");




//-----------------------FUNÇÃO PARA SELECIONAR LINHA DA TABELA-----------------------//
var tabela = document.getElementById("tabela");
var linhas = tabela.getElementsByTagName("tr");

for(var i = 0; i < linhas.length; i++){
	var linha = linhas[i];
  linha.addEventListener("click", function(){
  	//Adicionar ao atual
		selLinha(this, false); //Selecione apenas um
                //selLinha(this, true); //Selecione quantos quiser
	});
}

/**
Caso passe true, você pode selecionar multiplas linhas.
Caso passe false, você só pode selecionar uma linha por vez.
**/
function selLinha(linha, multiplos){ 
  if(!multiplos){
  	var linhas = linha.parentElement.getElementsByTagName("tr");
        for(var i = 0; i < linhas.length; i++){
          var linha_ = linhas[i];
          linha_.classList.remove("selecionado");    
        }
  }
  linha.classList.toggle("selecionado");
}

/* Seleção dos dados na tabela para alteração */
var btnVisualizar = document.getElementById("visualizarDados");

btnVisualizar.addEventListener("click", function(){
	var selecionados = tabela.getElementsByClassName("selecionado");
  //Verificar se está selecionado
  if(selecionados.length < 1){
  	alert("Selecione pelo menos uma linha");
    document.getElementById("alterar").setAttribute("style", "display: none;");
    return false;
  }else{
    document.getElementById("alterar").removeAttribute("style", "display: none;");
  }

  var dados_id = "";
  var dados_local = "";
  var dados_solicitante = "";
  var dados_deparmento = "";
  var dados_observacoes = "";
  var dados_horarios = "";
  var dados_status = "";
  var dados_equipamentos = "";

  for(var i = 0; i < selecionados.length; i++){
  	var selecionado = selecionados[i];
    selecionado = selecionado.getElementsByTagName("td");

    dados_id += selecionado[0].innerHTML;
    dados_local += selecionado[1].innerHTML;
    dados_solicitante += selecionado[3].innerHTML;
    dados_deparmento += selecionado[4].innerHTML;
    dados_observacoes += selecionado[7].innerHTML;
    dados_horarios += selecionado[2].innerHTML;
    dados_status += selecionado[6].innerHTML;
    dados_equipamentos += selecionado[5].innerHTML;
  }


  // ============================================================= \\
  document.getElementById("local").setAttribute("value", dados_local);
  document.getElementById("solicitante").setAttribute("value", dados_solicitante);
  document.getElementById("observacoes").setAttribute("value", dados_observacoes);
  document.getElementById("horario_inicio").setAttribute("value", dados_horarios.substring(0, dados_horarios.length - 8))
  document.getElementById("horario_fim").setAttribute("value", dados_horarios.substring(8, dados_horarios.length))

  // Seleção de um dos departamentos(DCEM, DTRA, DCHEL e OUTROS)
  if(dados_deparmento == "DCEN"){
    document.getElementById("selecao_dtra").removeAttribute("selected", 'selected');
    document.getElementById("selecao_dchel").removeAttribute("selected", 'selected');
    document.getElementById("selecao_outros").removeAttribute("selected", 'selected');
    document.getElementById("selecao_dcen").setAttribute("selected", 'selected');
  }else if(dados_deparmento == "DTRA"){
    document.getElementById("selecao_dcen").removeAttribute("selected", 'selected');
    document.getElementById("selecao_dchel").removeAttribute("selected", 'selected');
    document.getElementById("selecao_outros").removeAttribute("selected", 'selected');
    document.getElementById("selecao_dtra").setAttribute("selected", 'selected');
  }else if(dados_deparmento == "DCHEL"){
    document.getElementById("selecao_dtra").removeAttribute("selected", 'selected');
    document.getElementById("selecao_dcen").removeAttribute("selected", 'selected');
    document.getElementById("selecao_outros").removeAttribute("selected", 'selected');
    document.getElementById("selecao_dchel").setAttribute("selected", 'selected');
  }else{
    document.getElementById("selecao_dtra").removeAttribute("selected", 'selected');
    document.getElementById("selecao_dchel").removeAttribute("selected", 'selected');
    document.getElementById("selecao_dcen").removeAttribute("selected", 'selected');
    document.getElementById("selecao_outros").setAttribute("selected", 'selected');
  }


  // =================== Quantidade dos equipamentos ==========================

  var quantidade_note = "0";
  var quantidade_som = "0";
  var quantidade_projetor = "0";
  var quantidade_outros = "0";

  // Converter variavel texto em HTML
  let parser = new DOMParser();
  let equipamentos_html = parser.parseFromString(dados_equipamentos, "text/html");

  var contem_note = equipamentos_html.getElementById("contem_note");
  var contem_som = equipamentos_html.getElementById("contem_som");
  var contem_projetor = equipamentos_html.getElementById("contem_projetor");
  var contem_outros = equipamentos_html.getElementById("contem_outros");

  // IFs para selecionar a quantidade de equipamentos e aleterar no html.

  if (contem_note !== null){
    quantidade_note = document.getElementById("contem_note").innerHTML;
  }
  if (contem_som !== null){
    quantidade_som = document.getElementById("contem_som").innerHTML;
  }
  if (contem_projetor !== null){
    quantidade_projetor = document.getElementById("contem_projetor").innerHTML;
  }
  if (contem_outros !== null){
    quantidade_outros = document.getElementById("contem_outros").innerHTML;
  }

  // Pega o valor da tag Label.
  // document.getElementById("contem_note").innerHTML;

  // Altera o valor da tag o Label.
  //document.getElementById("contem_note").innerHTML = "9";

  // console.log("ID: " + dados_id)
  // console.log("Note: " + quantidade_note);
  // console.log("Som: " + quantidade_som);
  // console.log("Projetor: " + quantidade_projetor);
  // console.log("Outros: " + quantidade_outros);
  document.getElementById("id_selecao").setAttribute("value", dados_id);
  document.getElementById("id_note").setAttribute("value", quantidade_note);
  document.getElementById("id_som").setAttribute("value", quantidade_som);
  document.getElementById("id_projetor").setAttribute("value", quantidade_projetor);
  document.getElementById("id_outros").setAttribute("value", quantidade_outros);

  // STATUS DO EQUIPAMENTO
  // Converter variavel texto em HTML
  let parser_status = new DOMParser();
  let status_html = parser_status.parseFromString(dados_status, "text/html");

  if (status_html.getElementById("emsala") !== null){
    //console.log("Em sala");
    document.getElementById("id_emsala").checked = true;
  }else if(status_html.getElementById("retirado") !== null){
    //console.log("Retirado");
    document.getElementById("id_retirado").checked = true;
  }else{
    //console.log("Reserva")
    document.getElementById("id_reserva").checked = true;
  }

});

/*-------------------------------*/



/* Seleção dos dados na tabela para exclusão */
var btnExcluir = document.getElementById("excluir_dados")

btnExcluir.addEventListener("click", function(){
	var selecionados = tabela.getElementsByClassName("selecionado");
  //Verificar se está selecionado
  if(selecionados.length < 1){
  	alert("Selecione pelo menos uma linha");
    document.getElementById("excluir").setAttribute("style", "display: none;");
    return false;
  }else{
    document.getElementById("excluir").removeAttribute("style", "display: none;");
  }

  var dados_id = "";

  for(var i = 0; i < selecionados.length; i++){
  	var selecionado = selecionados[i];
    selecionado = selecionado.getElementsByTagName("td");

    dados_id += selecionado[0].innerHTML;

  }

  // console.log("ID: " + dados_id)
  document.getElementById("id_exclusao").setAttribute("value", dados_id);


});