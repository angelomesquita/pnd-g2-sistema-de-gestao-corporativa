# funcionarios/relatorios.py
# módulo de relatórios de funcionários

from .cadastro import funcionarios

def gerar_relatorio_funcionarios():
    print("Relatório de Funcionários:")
    for funcionario in funcionarios:
        print(f"Nome: {funcionario['nome']}, Cargo: {funcionario['cargo']}, Salário: {funcionario['salario']:.2f}")