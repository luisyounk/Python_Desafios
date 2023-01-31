# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input("Digite um numero até 9999: "))
print(f'Analisando o numero {num}')
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Temos {u} unidades')
print(f'Temos {d} dezenas')
print(f'Temos {c} centenas')
print(f'E temos {m} milhares')

