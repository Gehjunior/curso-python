'''
# Peça ao usuário para digitar três valores inteiros e imprima a soma deles.
'''
import os


def soma(n1, n2, n3):
    return n1+n2+n3


print('\n Abaixo informe três valores a serem somados. \n')
n1 = int(input('Informe o primeiro valor: \n'))
n2 = int(input('Informe o segundo valor: \n'))
n3 = int(input('Informe o terceiro valor: \n'))
print(f'A soma dos valores digitados é: {soma(n1,n2,n3)}')

os.system("pause")
