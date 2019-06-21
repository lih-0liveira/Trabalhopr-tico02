def main():
    ref_arquivo = open("usuarios.txt","r")
    arquivo = open('relatorio.txt', 'w')
    arquivo.write('ACME Inc.\t   Uso do espaço em disco pelos usuários\n')
    arquivo.write('------------------------------------------------------------\n')
    arquivo.write('Nr. \tUsuário \tEspaço utilizado\t % do uso')
    with open('usuarios.txt', 'r') as f:
        i =len(f.readlines())
        aux=0
        pass
    total = 0
    for linha in ref_arquivo:
        valores = linha.split()
        if (aux<=i):
            aux=aux+1
            a = str(aux)
            b = str(valores[0])
            arquivo.write('\n')
            arquivo.write(a)
            arquivo.write('\t')
            arquivo.write(b)
            from funcoes import Funcao
            num=float(valores[1])
            c=Funcao()
            c1=float('%.2f' % c.retornaEspaço(num) )
            d= str(c1)
            arquivo.write('    \t')
            arquivo.write(d)
            arquivo.write('\tMB')
            c2= float('%3.2f' % c.retornaPorcentagem(c1))
            e = str(c2)
            arquivo.write('    \t\t')
            arquivo.write(e)
            arquivo.write('%')
            total = total + c1
    medio = total/i
    total1=str(total)
    arquivo.write('\n\nEspaço total ocupado: ')
    arquivo.write(total1)
    arquivo.write('\tMB')
    arquivo.write('\nEspaço médio ocupado: ')
    aux3=float('%.2f' % medio)
    medio1=str(aux3)
    arquivo.write(medio1)
    arquivo.write('\tMB')
    arquivo.close()
main()
