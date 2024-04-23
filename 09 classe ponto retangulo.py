class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def imprimir(self):
        print(f"Ponto: ({self.x}, {self.y})")

class Retangulo:
    def __init__(self, largura, altura, ponto_inicial=0):
        self.largura = largura
        self.altura = altura
        self.ponto_inicial = ponto_inicial
    
    def encontrar_centro(self):
        x_centro = self.ponto_inicial.x + self.largura / 2
        y_centro = self.ponto_inicial.y + self.altura / 2
        return Ponto(x_centro, y_centro)

ponto_inicial = Ponto
x = input("Informe a primeira coordenada: ") 
y = input("Informe a segunda coordenada: ") 
largura = input("Informe a largura: ") 
altura = input("Informe a altura: ") 
    
retangulo = Retangulo(largura, altura)

print(f'Ponto central é: {retangulo.encontrar_centro}')