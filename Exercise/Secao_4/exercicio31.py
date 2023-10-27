'''
# Leia um número inteiro e imprima o seu antecessor e seu sucessor;
'''
import os

num = int(input('Informe um número: '))
antecessor = num - 1
sucessor = num + 1
print(f'O Antecessor de {num} é: {antecessor} \nE o seu Sucessor é {sucessor}')

os.system("pause")
