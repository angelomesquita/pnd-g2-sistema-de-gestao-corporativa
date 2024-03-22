# funcionarios/folha_pagamento.py
# módulo de folha de pagamento de funcionários

from .cadastro import funcionarios

def calcular_salarios():
    total_salarios = sum(funcionario["salario"] for funcionario in funcionarios)
    print(f"Total de salários a serem pagos: R$ {total_salarios:.2f}")   