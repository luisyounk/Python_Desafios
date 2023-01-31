# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras sem considerar espaços.
# – Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: '))
nome_uppe = (nome.upper())
nomelow = (nome.lower())
nome_st = (nome.split())
nome_nspc = (nome.replace(" ",""))

print(f'Seu nome é {nome} \n'
      f'Tudo maisculo {nome_uppe}\n'
      f'Tudo minusculo {nomelow}\n'
      f'Seu nome tem {len(nome_nspc)} sem contar espaços.\n'
      f'Seu primeiro nome tem {len(nome.split()[0])} letras')

