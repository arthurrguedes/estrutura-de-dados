class Macaco:
    def __init__(self, nome): #cade  o estomago no construtor?
        self.nome = nome
        self.estomago = [] 

    def comer(self, alimento):
        self.estomago.append(alimento)
        print(f"{self.nome} comeu {alimento}.")

    def verEstomago(self):
        if self.estomago:
            print(f"{self.nome} tem no estômago: {', '.join(self.estomago)}")
        else:
            print(f"{self.nome} Estômago está vazio.")

    def digerir(self):
        if self.estomago:
            print(f"{self.nome} está digerindo {', '.join(self.estomago)}.")
            self.estomago = []
        else:
            print(f"{self.nome} não tem nada para digerir.")


macaco1 = Macaco("Vitor")
macaco2 = Macaco("Olivia")

macaco1.comer("banana")
macaco2.comer("maçã")
macaco1.comer("laranja")
macaco2.comer("uva")

macaco1.verEstomago()
macaco2.verEstomago()

macaco1.digerir()
macaco2.digerir()

macaco1.verEstomago()
macaco2.verEstomago()

macaco1.comer("Olivia")
macaco1.verEstomago()