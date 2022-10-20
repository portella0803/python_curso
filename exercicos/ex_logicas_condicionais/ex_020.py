n1 = float(input('Digite o valor de A:'))
n2 = float(input('Digite o valor de B:'))
n3 = float(input('Digite o valor de C:'))

# Verificar se é um triagulo
if n1 + n2 < n3 or n1 + n3 < n2 or n3 + n2 < n1:
    print('É um triângulo')
elif n1 == n2 == n3:
    print('Triângulo Equilátero')
elif n1 == n2 or n2 == n3 or n3 == n1:
    print('Triângulo Isósceles')
elif n1 != n2 and n2 != n3 and n3 != n1:
    print('Triângulo Escaleno')
else:
    print('Não é um triângulo')
