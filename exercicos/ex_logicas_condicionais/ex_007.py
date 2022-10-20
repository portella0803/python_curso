num1 = float(input('Digite um número:\n'))
num2 = float(input('Digite um outro número:\n'))

if num1 > num2:
    print(f'O maior número é o {num1}')
elif num1 == num2:
    print('Os números são iguais.')
else:
    print(f'O maior número é o {num2}')
