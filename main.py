# main.py

# importações dos módulos usados do pacote funcionário
from funcionarios import cadastro as func_cadastro
from funcionarios import folha_pagamento as func_folha
from funcionarios import relatorios as func_relatorios
# importações dos módulos usados do pacote financeiro
from financeiro import contas_pagar as fin_contas_pagar
from financeiro import contas_receber as fin_contas_receber
from financeiro import relatorios as fin_relatorios

print("Bem-vindo ao Sistema de Gestão Corporativa")

print("\n--- Funcionários ---")
func_cadastro.cadastrar_funcionario("João", "Desenvolvedor", 5000)
func_cadastro.cadastrar_funcionario("Maria", "Desenvolvedor", 10000)
func_cadastro.cadastrar_funcionario("José", "Estagiário", 1200)
func_cadastro.cadastrar_funcionario("Ruth", "Diretora", 20000)
func_folha.calcular_salarios()
func_relatorios.gerar_relatorio_funcionarios()

print("\n--- Financeiro ---")
fin_contas_pagar.registrar_conta(1000, "Aluguel")
fin_contas_pagar.registrar_conta(500, "Energia")
fin_contas_receber.registrar_conta(2000, "Cliente A")
fin_contas_receber.registrar_conta(5000, "Cliente B")
fin_relatorios.gerar_relatorio_financeiro()