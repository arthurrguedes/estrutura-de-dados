class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo_inicial, taxa_juros):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros

    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome

    def taxa_juros(self):
        return self.taxa_juros

    def adicione_juros(self):
        juros = self.saldo * (self.taxa_juros / 100)
        self.saldo += juros

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def saque(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

conta_poupanca = ContaCorrente(numero_conta="12345", nome_correntista="Fulano", saldo_inicial=1000.00, taxa_juros=10)

print(f"Saldo inicial da conta: R${conta_poupanca.saldo:.2f}")

conta_poupanca.adicione_juros()
conta_poupanca.deposito(500)
conta_poupanca.saque(200) 

print(f"Saldo atual da conta: R${conta_poupanca.saldo:.2f}")