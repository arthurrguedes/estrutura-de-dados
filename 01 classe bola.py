class Bola:
    def __init__(self, cor=None, circ=0, material=None):
        self.cor = cor
        self.circ = circ
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        print(self.cor)
        return self.cor

   #def trocaCirc(self, nova_circ):
       #self.circ = nova_circ

   #def mostraCirc(self):
       #print(self.circ)
       #return self.circ

    #def trocaMaterial(self, novo_material):
       #self.material = novo_material

    #def mostraMaterial(self):
       #print(self.material)
       #return self.material

# criando o objeto
bola_senac = Bola('Vermelha', 30, "Borracha")
bola_senac.trocaCor('Azul')
#bola_senac.trocaCirc(25)
#bola_senac.trocaMaterial("Plástico")
bola_senac.mostraCor()
#bola_senac.mostraCirc()
#bola_senac.mostraMaterial()


