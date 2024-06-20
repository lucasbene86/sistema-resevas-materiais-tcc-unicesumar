//>>>>>>>>>>>>>>>>>>>>>>> FUNÇÃO PARA VERIFICAR SENHA <<<<<<<<<<<<<<<<<<<<<<<<//

function validarSenha(name1, name2)
{
    var senha1 = document.getElementById(name1).value;
    var senha2 = document.getElementById(name2).value;
		
    if (senha1 != "" && senha2 != "" && senha1 === senha2)
    {
    	// console.log('Senha igual!')
      document.getElementById("botao_adicionar").disabled = false;
      document.getElementById("senha_incorreta").setAttribute("style", "display: none;");
      // document.getElementById("botao_adicionar").setAttribute("style", "display: none;");
    }
    else
    {
      document.getElementById("botao_adicionar").disabled = true;
      document.getElementById("senha_incorreta").setAttribute("style", "display: flex;");
      // console.log('Senha incorreta!!')
    }
} 



//>>>>>>>>>>>>>>>>>>>>>>> FUNÇÃO PARA SELECIONAR LINHA DA TABELA <<<<<<<<<<<<<<<<<<<<<<<<//
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


//----------------------------------------------------------------------------------------//
//>>>>>>>>>>>>>>>>>>>> FUNÇÃO PARA SELECIONAR LINHA DA TABELA E APAGAR <<<<<<<<<<<<<<<<<<<//
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


//----------------------------------------------------------------------------------------//
//>>>>>>>>>>>>>>>>>>>>>>>>> FUNÇÃO PARA ALTERAR DADOS <<<<<<<<<<<<<<<<<<<<<<<<<<<//
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
  var dados_login = "";
  var dados_nome = "";
  var dados_status = "";

  for(var i = 0; i < selecionados.length; i++){
  	var selecionado = selecionados[i];
    selecionado = selecionado.getElementsByTagName("td");

    dados_id += selecionado[0].innerHTML;
    dados_login += selecionado[2].innerHTML;
    dados_nome += selecionado[1].innerHTML;
    dados_status += selecionado[4].innerHTML;
  }

  //console.log("ID: " + dados_id)
  //console.log("Login: " + dados_login)
  //console.log("Nome: " + dados_nome)
  //console.log("Status: " + dados_status.substring(51, dados_status.length - 2))
  dados_status = dados_status.substring(51, dados_status.length - 2)

  // ============================================================= \\
  document.getElementById("id_selecao").setAttribute("value", dados_id);
  document.getElementById("nome").setAttribute("value", dados_nome);
  document.getElementById("login").setAttribute("value", dados_login);


  // Seleção do status (ATIVO ou INATIVO)
  if(dados_status == "on"){
    document.getElementById("inativo").removeAttribute("checked", 'checked');
    document.getElementById("ativo").setAttribute("checked", 'checked');
  }else if(dados_status == "off"){
    document.getElementById("ativo").removeAttribute("checked", 'checked');
    document.getElementById("inativo").setAttribute("checked", 'checked');
  }

});

/*------------------------------------------------------------------------------------*/