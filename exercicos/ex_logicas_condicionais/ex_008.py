nota1 = float(input('Digite a primeira nota:\n'))
nota2 = float(input('Digite a segunda nota:\n'))

if 0 <= nota2 and nota2 <= 10:
    print(f'Amédia dessas notas é igual a {(nota1 + nota2) / 2}')
else:
    print('[ERRO] - A nota deve ser entre 0.0 e 10.0')
