altura = float(input('Diga sua altura:\n'))
peso = float(input('Diga seu peso:\n'))

# Menor que 1.20
if altura < 1.20 and peso <= 60:
    print('Sua classificação é A')
elif altura < 1.20 and peso >= 60 or peso <= 90:
    print('Sua classificação é D')
elif altura < 1.20 and peso > 90:
    print('Sua classificação é G')
else:
    print('[ERRO]')

# De 1.20 a 1.70
if altura > 1.20 or altura <= 1.70 and peso <= 60:
    print('Sua classificação é B')
elif altura > 1.20 or altura <= 1.70 and peso >= 60 or peso <= 90:
    print('Sua classificação é E')
elif altura > 1.20 or altura <= 1.70 and peso > 90:
    print('Sua classificação é H')
else:
    print('[ERRO]')

# Maior que 1.70
if altura > 1.70 and peso <= 60:
    print('Sua classificação é C')
elif altura > 1.70 and peso >= 60 or peso <= 90:
    print('Sua classificação é F')
elif altura > 1.70 and peso > 90:
    print('Sua classificação é I')
else:
    print('[ERRO]')
