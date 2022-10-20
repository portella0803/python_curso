import math

num = float(input('Digite um número:\n'))

if num > 0:
    print(f'A raiz quadrada desse número é igual a {math.pow(num, 1 / 2)}')
    print(f'Esse número ao quadrado é igual a {num ** 2}')
if num < 0:
    print('[ERRO] - Número inválido, tente novamente!')
