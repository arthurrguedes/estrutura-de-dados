class Quadrado:
    def __init__(self, tamanholado=20):
        self.tamanholado=tamanholado

    def mudarLado(self,novo_lado):
        self.tamanholado = novo_lado

    def retornarLado(self):
        print(self.tamanholado)
        return self.tamanholado
    def calcarea(self):
        return self.tamanholado ** 2

# criando o objeto
quadradinho = Quadrado(30)
quadradinho.mudarLado(14)
print(quadradinho.tamanholado)
print(quadradinho.calcarea())




