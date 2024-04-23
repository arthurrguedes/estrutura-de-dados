class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def set_mudar_lados(self, nova_base, nova_altura):
        self.base = nova_base
        self.altura = nova_altura

    def get_retornar_lados(self):
        return self.base, self.altura

    def get_calcular_area(self):
        return self.base * self.altura

    def get_calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    

base_quarto = float(input("Informe a largura do local em metros: "))
altura_quarto = float(input("Informe a altura do local em metros: "))
#objeto
quarto = Retangulo(base_quarto, altura_quarto)
area_quarto = quarto.get_calcular_area()
pisos = area_quarto
perimetro_quarto = quarto.get_calcular_perimetro()
rodapes = perimetro_quarto

print(f"Quantidade de pisos necessários: {pisos} metros quadrados")
print(f"Quantidade de rodapés necessários: {rodapes} metros")

