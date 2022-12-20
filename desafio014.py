##Calcular Seno Cosseno e Tangente

import math
angulo = float(input('Digite o ângulo que você deseja:'))
seno = math.sin(math.radians(angulo))
print(f'O ângulo {angulo} tem o SENO {seno:,.2f}')
cosseno = math.cos(math.radians(angulo))
print(f'O ângulo {angulo} tem o COSSENO de {cosseno:,.2f}');
tangente = math.tan(math.radians(angulo))
print(f'O ângulo {angulo} tem a TANGENTE {tangente:,.2f}')
