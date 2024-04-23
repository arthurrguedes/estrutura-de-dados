class Carro:
    def __init__(self, consumo_km_por_litro):
        self.consumo_km_por_litro = consumo_km_por_litro
        self.combustivel_no_tanque = 0

    def andar(self, distancia):
        consumo_total = distancia / self.consumo_km_por_litro
        if consumo_total <= self.combustivel_no_tanque:
            self.combustivel_no_tanque -= consumo_total
            print(f"O carro andou {distancia} km.")
        else:
            print("Combustível insuficiente para percorrer essa distância.")

    def obter_gasolina(self):
        return self.combustivel_no_tanque

    def adicionar_gasolina(self, quantidade):
        self.combustivel_no_tanque += quantidade
        print(f"Abastecido {quantidade} litros de gasolina. Novo total: {self.combustivel_no_tanque} litros.")

carro = Carro(consumo_km_por_litro=10)

carro.adicionar_gasolina(50)

carro.andar(600)
print("Nível de combustível:", carro.obter_gasolina())