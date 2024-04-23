class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, qtd_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.qtd_combustivel = qtd_combustivel

    def abastecer_por_valor(self, valor_abastecido):
        qtd_abastecida = valor_abastecido / self.valor_litro
        if qtd_abastecida <= self.qtd_combustivel:
            self.qtd_combustivel -= qtd_abastecida
            print(f"Abastecido {qtd_abastecida:.2f} litros de {self.tipo_combustivel}.")
        else:
            print("Quantidade de combustível insuficiente na bomba.")

    def abastecer_por_litro(self, qtd_litros):
        valor_pagar = qtd_litros * self.valor_litro
        if qtd_litros <= self.qtd_combustivel:
            self.qtd_combustivel -= qtd_litros
            print(f"Valor a pagar: R${valor_pagar:.2f}.")
        else:
            print("Quantidade de combustível insuficiente na bomba.")

    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor

    def alterar_combustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel

    def alterar_qtd_combustivel(self, nova_quantidade):
        self.qtd_combustivel = nova_quantidade
    
bomba1 = BombaCombustivel("Gasolina", 5.0, 1000)

while True:
    print("\n--- Menu ---")
    print("1. Abastecer por valor")
    print("2. Abastecer por litro")
    print("3. Alterar valor do litro")
    print("4. Alterar tipo de combustível")
    print("5. Alterar quantidade de combustível na bomba")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor_abastecido = float(input("Informe o valor a ser abastecido: "))
        bomba1.abastecer_por_valor(valor_abastecido)
    elif opcao == "2":
        qtd_litros = float(input("Informe a quantidade em litros: "))
        bomba1.abastecer_por_litro(qtd_litros)
    elif opcao == "3":
        novo_valor = float(input("Informe o novo valor do litro: "))
        bomba1.alterar_valor(novo_valor)
    elif opcao == "4":
        novo_combustivel = input("Informe o novo tipo de combustível: ")
        bomba1.alterar_combustivel(novo_combustivel)
    elif opcao == "5":
        nova_qtd = float(input("Informe a nova quantidade de combustível: "))
        bomba1.alterar_qtd_combustivel(nova_qtd)
    elif opcao == "6":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
