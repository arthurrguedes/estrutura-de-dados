class Tamagushi:
    def __init__(self, nome="Undefined", fome=0, saude=0, idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
        return self.nome

    def alterar_fome(self, nova_fome):
        self.fome = nova_fome
        return self.fome

    def alterar_saude(self, nova_saude):
        self.saude = nova_saude
        return self.saude

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade
        return self.idade

    def set_humor(self):
        humor = (self.fome + self.saude) / 2
        return humor
    


pandolfo = Tamagushi("Pandolfo", 6, 5, 2)
print(f"Nome: {pandolfo.nome}, Fome: {pandolfo.fome}, Saúde: {pandolfo.saude}, Idade: {pandolfo.idade}, Humor: {pandolfo.set_humor()}")
pandolfo.alterar_fome(10)
pandolfo.alterar_saude(9)
pandolfo.alterar_idade(3)

print(f"Nome: {pandolfo.nome}, Fome: {pandolfo.fome}, Saúde: {pandolfo.saude}, Idade: {pandolfo.idade}, Humor: {pandolfo.set_humor()}")
