class Televisor:
    def __init__(self):
        self.canal = 1
        self.volume = 5

    def mudar_canal(self, novo_canal):
        if 1 <= novo_canal <= 30:
            self.canal = novo_canal
            print(f"Canal alterado para {novo_canal}")
        else:
            print("Canal inexistente. Escolher entre 1 e 30.")

    def aumentar_volume(self):
        if self.volume < 25:
            self.volume += 1
            print(f"Volume aumentado para {self.volume}")
        else:
            print("Volume máximo atingido.")

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print(f"Volume diminuído para {self.volume}")
        else:
            print("Volume mínimo atingido.")

tv = Televisor()

while True:
    print("- Controle Remoto -")
    print("1. Mudar Canal")
    print("2. Aumentar Volume")
    print("3. Diminuir Volume")
    print("4. Desligar TV")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        novo_canal = int(input("Informe o número do canal: "))
        tv.mudar_canal(novo_canal)
    elif opcao == "2":
        tv.aumentar_volume()
    elif opcao == "3":
        tv.diminuir_volume()
    elif opcao == "4":
        print("Desligando TV...")
        break
    else:
        print("Opção inválida. Tente novamente.")