'''
# Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro;
'''
import os

num = int(input('Informe um número: '))
soma_st_ad = ((num * 3) + 1) + ((num * 2) - 1)
print(
    f'A soma do sucessor do seu triplo com o antecessor do seu dobro é: {soma_st_ad}')

os.system("pause")
