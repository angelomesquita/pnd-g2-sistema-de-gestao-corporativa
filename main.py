# main.py

# importações dos módulos usados do pacote funcionário
from funcionarios import cadastro as func_cadastro
from funcionarios import folha_pagamento as func_folha
from funcionarios import relatorios as func_relatorios
# importações dos módulos usados do pacote financeiro
from financeiro import contas_pagar as fin_contas_pagar
from financeiro import contas_receber as fin_contas_receber
from financeiro import relatorios as fin_relatorios

def main(): 
    print("Bem-vindo ao Sistema de Gestão Corporativa")

    while True:
        print("\nOpções: ")
        print("1. Cadastrar funcionário")
        print("2. Calcular salários")
        print("3. Registrar conta a pagar")
        print("4. Registrar conta a receber")
        print("5. Gerar relatórios")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            func_cadastro.cadastrar_funcionario()
        elif opcao == '2':
            func_folha.calcular_salarios()
        elif opcao == '3':
            fin_contas_pagar.registrar_conta()
        elif opcao == '4':
            fin_contas_receber.registrar_conta()
        elif opcao == '5':
            func_relatorios.gerar_relatorio_funcionarios()
            fin_relatorios.gerar_relatorio_financeiro()
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida...")

if __name__ == "__main__":
    main()