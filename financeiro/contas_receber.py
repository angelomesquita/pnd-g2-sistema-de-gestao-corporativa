# financeiro/contas_receber.py
# módulo de contas a receber da empresa

contas_receber = []

def registrar_conta():
    valor = float(input("Digite o valor da conta a receber"))
    descricao = input("Digite a descrição da conta a receber")
    
    conta = {"valor": valor, "descricao": descricao}
    contas_receber.append(conta)
    print(f"Conta a receber '{descricao}' registrada no valor de R$ {valor:.2f}")