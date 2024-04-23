class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
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
    
    def calcular_humor(self):
        humor = (self.fome + self.saude) / 2
        return humor
    
    def alimentar(self, quantidade_comida):
        self.saude += quantidade_comida / 2
        self.fome -= quantidade_comida
    
    def brincar(self, tempo_brincadeira):
        self.fome -= tempo_brincadeira / 2
        self.saude -= tempo_brincadeira / 3


tamagushi1 = Tamagushi("Pandolfo", 10, 80, 3)

print("Nome:", tamagushi1.nome)
print("Fome:", tamagushi1.fome)
print("Saúde:", tamagushi1.saude)
print("Idade:", tamagushi1.idade)
print("Humor:", tamagushi1.calcular_humor())

tamagushi1.alimentar(20)
tamagushi1.brincar(10)

print("Após alimentação e brincadeira:")
print("Fome:", tamagushi1.fome)
print("Saúde:", tamagushi1.saude)
print("Humor:", tamagushi1.calcular_humor())
