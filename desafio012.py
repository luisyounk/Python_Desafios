// Criar um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira


import math
num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e a sua porção inteira é {math.trunc(num)}')
