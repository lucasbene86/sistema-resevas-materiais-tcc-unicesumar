# Modulo para verificar nível do usuario.

def nivel_usuario(dado):
    nivel_1 = '1'
    nivel_2 = '2'

    if str(dado) == 'funcionario':
        return nivel_1
    else:
        return nivel_2
    