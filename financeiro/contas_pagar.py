# financeiro/contas_pagar.py
# módulo de contas a pagar da empresa

contas_pagar = []

def registrar_conta(valor, descricao):
    conta = {"valor": valor, "descricao": descricao}
    contas_pagar.append(conta)
    print(f"Conta a pagar '{descricao}' registrada no valor de R$ {valor:.2f}")
