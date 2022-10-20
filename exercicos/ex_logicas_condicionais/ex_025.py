import math

print('Equaçao do 2o grau da forma: ax² + bx + c')

a = int(input('Coeficiente a: '))

if (a == 0):
    print('Se a=0, não é equação do segundo grau. Tchau')
else:
    b = int(input('Coeficiente b: '))
    c = int(input('Coeficiente c: '))
    delta = b * b - (4 * a * c)

    if delta < 0:
        print('Delta menor que 0. Raízes imaginárias. Tchau')
    elif delta == 0:
        raiz = -b / (2 * a)
        print('Delta=0 , raiz = ', raiz)
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print('Raizes: ', raiz1, ' e ', raiz2)