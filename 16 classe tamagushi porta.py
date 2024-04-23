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
    
    def __str__(self):
        return f"Nome: {self.nome}\nFome: {self.fome}\nSaúde: {self.saude}\nIdade: {self.idade}"


pandolfo = Tamagushi("Pandolfo", 6, 5, 2)

while True:
        print("\nMenu:")
        print("1. Alterar Nome")
        print("2. Alterar Fome")
        print("3. Alterar Saúde")
        print("4. Alterar Idade")
        print("5. Mostrar Informações")
        print("6. Opção Secreta")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            novo_nome = input("Digite o novo nome: ")
            pandolfo.alterar_nome(novo_nome)
        elif opcao == "2":
            nova_fome = int(input("Digite o valor para alterar a fome: "))
            pandolfo.alterar_fome(nova_fome)
        elif opcao == "3":
            nova_saude = int(input("Digite o valor para alterar a saúde: "))
            pandolfo.alterar_saude(nova_saude)
        elif opcao == "4":
            nova_idade = int(input("Digite o valor para alterar a idade: "))
            pandolfo.alterar_idade(nova_idade)
        elif opcao == "5":
            print(pandolfo)
        elif opcao == "6":
            senha = input("Digite a senha para acessar a opção secreta: ")
            if senha == "senha_secreta":
                print("Valores exatos dos atributos do Tamagushi:")
                print(pandolfo.__dict__)
            else:
                print("Senha incorreta! Acesso negado.")
        else:
            print("Opção inválida!")
