def main():
    print ('Bem vindo ao programa!')
    numero = int( input('\nDigite um número inteiro de 4 dígitos, cada um entre 0 e 9 :'))

    if(numero>9999):
        print ('\nNúmero inválido !')
        numero = int( input('\nTente novamente:'))

    from criptografia import Criptografia
    #Encontrando os dígitos
    i = Criptografia
    aux = numero
    dig1 = i.digitos(aux,1000)
    aux = aux - dig1*1000
            
    dig2 = i.digitos(aux,100)
    aux = aux - dig2*100

    dig3 = i.digitos(aux,10)
    aux = aux - dig3*10

    dig4 = aux
        
    print('\nFunções: \n(1) Criptografar\n(2) Descriptografar')
    escolha = input()
    if(escolha != '1' and escolha != '2'):
        print ('Escolha inválida!')
        escolha = input('\nTente novamente:')

    if(escolha == '1'):
        #Criptografando
        dig1 = i.criptografarNumero(dig1)
        dig2 = i.criptografarNumero(dig2)
        dig3 = i.criptografarNumero(dig3)
        dig4 = i.criptografarNumero(dig4)

        #Trocando os digitos 1 e 3, 2 e 4
        aux2 = dig1
        dig1=dig3
        dig3=aux2

        aux2=dig2
        dig2=dig4
        dig4=aux2

        novo = dig1*1000 + dig2*100 + dig3*10 + dig4
        print ('Número criptografado:', novo)

    if(escolha == '2'):
        #Destrocando os digitos 1 e 3, 2 e 4
        aux2 = dig1
        dig1=dig3
        dig3=aux2

        aux2=dig2
        dig2=dig4
        dig4=aux2
        
        #Descriptografando
        dig1 = i.descriptografarNumero(dig1)
        dig2 = i.descriptografarNumero(dig2)
        dig3 = i.descriptografarNumero(dig3)
        dig4 = i.descriptografarNumero(dig4)

        novo = dig1*1000 + dig2*100 + dig3*10 + dig4
        print ('Número descriptografado:', novo)
        
    input("Pressione <enter> para continuar")
    
main()

