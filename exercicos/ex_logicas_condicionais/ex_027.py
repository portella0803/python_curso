import math

n1 = int(input('Digite um número:\n'))
n2 = int(input('Digite um número:\n'))
n3 = int(input('Digite um número:\n'))

opcao = int(input('1 - Média Geométrica\n2 - Média Ponderada\n3 - Média Harmônica\n4 - Média Aritmética\n'))

if opcao == 1:
    raiz = n1 * n2 * n3
    media = raiz ** (1/3)
    print(f'A média Geométrica é igual a {media}')
elif opcao == 2:
    media = (n1 + 2 * n2 + 3 * n3) / 6
    print(f'A média Ponderada é igual a {media}')
elif opcao == 3:
    media = 1 / (1/n1 + 1/n2 + 1/n3)
    print(f'A média Harmônica é igual a {media}')
else:
    media = (n1 + n2 + n3) / 3
    print(f'A média Aritmética é igual a {media}')
