import math

num = float(input('Digite um número:\n'))

if num > 0:
    raiz = math.pow(num, 1 / 2)
    print(raiz)
if num < 0:
    print(f'Esse número ao quadrado é igual a {num ** 2}.')
