ano = int(input('Digite o ano:\n'))

r1 = ano % 400
r2 = ano % 4
r3 = ano % 100

if r1 == 0 or r2 == 0 and r3 != 0:
    print('Esse ano é bissexto')
else:
    print('Esse ano não é bissexto')
