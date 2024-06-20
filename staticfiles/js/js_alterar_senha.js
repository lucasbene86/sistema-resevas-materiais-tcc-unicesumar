//>>>>>>>>>>>>>>>>>>>>>>> FUNÇÃO PARA VERIFICAR SENHA <<<<<<<<<<<<<<<<<<<<<<<<//

function validarSenha(name1, name2)
{
    var senha1 = document.getElementById(name1).value;
    var senha2 = document.getElementById(name2).value;
		
    if (senha1 != "" && senha2 != "" && senha1 === senha2)
    {
      console.log('Senha igual!')
      document.getElementById("botao_alterar").disabled = false;
      document.getElementById("senha_incorreta").setAttribute("style", "display: none;");
    }
    else
    {
      document.getElementById("botao_alterar").disabled = true;
      document.getElementById("senha_incorreta").setAttribute("style", "display: flex;");
      console.log('Senha incorreta!!')
    }
}