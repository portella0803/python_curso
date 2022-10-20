h = float(input('Digite a sua altura:\n'))
sexo = input('Se você for do sexo masculino digite m e se for do feminino digite f:\n').upper()

if sexo == 'm':
    print(f'Seu peso ideal seria: {(72.7 * h) -58}')
else:
    print(f'Seu peso ideal seria: {(62.1 * h) - 44.7}')