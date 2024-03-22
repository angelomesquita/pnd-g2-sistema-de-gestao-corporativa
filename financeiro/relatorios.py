# financeiro/relatorios.py
# módulo de relatórios do financeiro da empresa

from .contas_pagar import contas_pagar
from .contas_receber import contas_receber

def gerar_relatorio_financeiro():
    total_contas_pagar = sum(conta['valor'] for conta in contas_pagar)
    total_contas_receber = sum(conta['valor'] for conta in contas_receber)
    print("Relatório Financeiro:")
    print(f"Total de contas a pagar: R$ {total_contas_pagar:.2f}")
    print(f"Total de contas a receber: R$ {total_contas_receber:.2f}")
