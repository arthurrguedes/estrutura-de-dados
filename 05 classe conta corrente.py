class ContaCorrente:
    def __init__(self, numero_conta=None, nome_correntista=None, saldo=0.00):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
        print(f'''Correntista: {self.nome_correntista} \n
Número da conta: {self.numero_conta} \n
Saldo: {self.saldo}''')

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo:.2f}")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente.")

    def mostrarsaldo(self):
        return self.saldo

conta = ContaCorrente('4555', "Arthur", 120.00)
conta.deposito(2000)
conta.saque(50)
print(conta.mostrarsaldo())
