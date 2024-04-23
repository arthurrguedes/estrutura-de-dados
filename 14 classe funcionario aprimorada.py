class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def obter_nome(self):
        return self.nome
    
    def obter_salario(self):
        return self.salario
    
    def aumentar_salario(self, porcentagem_aumento):
        aumento = self.salario * (porcentagem_aumento / 100)
        self.salario += aumento


funcionario1 = Funcionario("Arthur", 3500.0)
    
print("Nome:", funcionario1.obter_nome())
print("Salário:", funcionario1.obter_salario())
    
funcionario1.aumentar_salario(10)
print("Novo salário após aumento:", funcionario1.obter_salario())