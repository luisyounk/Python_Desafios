# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite um nome: ')).upper()
print(f'Seu nome tem Silva? {"SILVA" in nome}')