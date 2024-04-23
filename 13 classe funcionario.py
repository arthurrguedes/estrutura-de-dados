class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def obter_nome(self):
        return self.nome

    def obter_salario(self):
        return self.salario

funcionario1 = Funcionario("João", 3000.00)

print("Nome do funcionário:", funcionario1.obter_nome())
print("Salário do funcionário:", funcionario1.obter_salario())
