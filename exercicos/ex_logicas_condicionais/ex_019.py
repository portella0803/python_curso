n = int(input('Digite um número inteiro\n'))

r1 = n % 3
r2 = n % 5

if r1 == 0:
    print('É divisivel por 3')
else:
    print('Não é divisivel por 3')
if r2 == 0:
    print('É divisivel por 5')
else:
    print('Não é divisivel por 5')
