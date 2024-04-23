class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.crescer(0.5 * anos)

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura


pessoa1 = Pessoa("Arthur", 18, 68, 170)
print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}, Peso: {pessoa1.peso}, Altura: {pessoa1.altura}cm")

pessoa1.envelhecer(1) 
pessoa1.engordar(3)
pessoa1.emagrecer(1)
print(f"Atualmente: Nome: {pessoa1.nome}, Idade: {pessoa1.idade}, Peso: {pessoa1.peso}, Altura: {pessoa1.altura}cm")

