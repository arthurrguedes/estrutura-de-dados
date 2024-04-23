class Bicho:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 10
        self.tedio = 10

    def alimentar(self):
        self.fome -= 5

    def brincar(self):
        self.tedio -= 5

    def ouvir(self):
        print(f"{self.nome} diz: Estou feliz!")

    def __str__(self):
        return f"Nome: {self.nome}, Fome: {self.fome}, Tédio: {self.tedio}"
    

class Fazenda:
    def __init__(self):
        self.animais = []

    def adicionar_animais(self, animal):
        self.animais.append(animal)

    def alimentar_todos(self):
        for animais in self.animais:
            animais.alimentar()

    def brincar_todos(self):
        for animais in self.animais:
            animais.brincar()

    def ouvir_todos(self):
        for animais in self.animais:
            animais.ouvir()

    def mostrar_status_todos(self):
        for animais in self.animais:
            print(animais)


fazenda = Fazenda()
        # Adicionando alguns bichinhos à fazenda
fazenda.adicionar_animais(Bicho("Cavalo"))
fazenda.adicionar_animais(Bicho("Ovelha"))
fazenda.adicionar_animais(Bicho("Porco"))

while True:
    print("\nMenu:")
    print("1. Alimentar todos os bichinhos")
    print("2. Brincar com todos os bichinhos")
    print("3. Ouvir todos os bichinhos")
    print("4. Mostrar status de todos os bichinhos")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        fazenda.alimentar_todos()
        print("Todos os bichinhos foram alimentados!")
    elif opcao == "2":
        fazenda.brincar_todos()
        print("Todos os bichinhos brincaram!")
    elif opcao == "3":
        fazenda.ouvir_todos()
    elif opcao == "4":
        fazenda.mostrar_status_todos()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
