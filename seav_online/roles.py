from rolepermissions.roles import AbstractUserRole

# Permissões para coordenador
class Administrador(AbstractUserRole):
    available_permissions = {'cadastrar_funcionarios': True, 'reservar_equipamentos': True}

# Permissões para coordenador
class Coordenador(AbstractUserRole):
    available_permissions = {'cadastrar_funcionarios': True, 'reservar_equipamentos': True}

# Permissões para funcionários
class Funcionario(AbstractUserRole):
    available_permissions = {'reservar_equipamentos': True}