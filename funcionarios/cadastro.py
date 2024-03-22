# funcionarios/cadastro.py
# módulo de cadastro de funcionários

funcionarios = []

def cadastrar_funcionario(nome, cargo, salario):
    funcionario = {"nome": nome, "cargo": cargo, "salario": salario}
    funcionarios.append(funcionario)
    print(f"Funcionário {nome} cadastrado com sucesso.")

#atualizar_funcionario()
#listar_funcionarios()
#buscar_funcionario()
#apagar_funcionario()