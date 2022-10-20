num1 = int(input('Digite um número inteiro:\n'))
num2 = int(input('Digite um outro número inteiro:\n'))

if num1 > num2:
    print(f'O {num1} é maior que {num2}')
    print(f'A diferença entre eles é igual a {num1 - num2}')
else:
    print(f'O {num2} é maior que {num1}')
    print(f'A diferença entre eles é igual a {num2 - num1}')
