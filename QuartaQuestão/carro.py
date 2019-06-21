class Carro(object):
    combustivel = 0
    
    def __init__(self, consumo):
        self.consumo = consumo
        pass

    def andar(self,distancia):
        self.combustivel = self.combustivel - distancia/self.consumo
        print ('Combustível gasto:', distancia/self.consumo, 'Litros')
        print ('Combustível disponível:', self.combustivel, 'Litros')
        pass

    def obterGasolina(self):
        print ('Combustível disponível:', self.combustivel, 'Litros')
        pass

    def adicionarGasolina(self,valor):
        aux = self.combustivel + valor
        self.combustivel = aux
        pass
