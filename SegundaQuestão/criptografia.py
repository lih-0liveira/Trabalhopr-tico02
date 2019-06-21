#Criptografando e Descriptografando o número
class Criptografia (object):
    def __init__(self, num):
        self.num = num

    def digitos(num,div):
        dig = int(num/div)
        return dig
    
    def criptografarNumero(valor):
        aux = (valor + 6) % 10
        return aux

    def descriptografarNumero(valor):
        for b in range(0, 2, 1):
            aux = 10*b + valor - 6
            if(aux>=0 and aux<10):
                aux2 = aux
        return aux2
