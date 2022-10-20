import math

num = float(input('Digite um número para saber sua raiz quadrada:\n'))

if num > 0:
    raiz = math.pow(num, 1 / 2)
    print(raiz)
if num < 0:
    print('[ERRO] - Número inválido, tente novamente!')
