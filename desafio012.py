#Criar um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import trunc
num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e a sua porção inteira é {trunc(num)}')


'''Poderia ser feito desse modo também
print(f'O valor digitado foi {num} e a sua porção inteira é {int(num)}')'''
