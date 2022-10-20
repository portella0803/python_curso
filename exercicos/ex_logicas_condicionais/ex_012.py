import math

x = int(input('Digite um número inteiro e positivo:\n'))

if x >= 0:
    print(f'O logaritimo desse número é igual a {math.log(x)}')
else:
    print('[ERRO] - Número Inválido!')
