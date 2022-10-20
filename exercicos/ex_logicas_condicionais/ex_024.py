valor = float(input('Digite o valor:\n'))
estado = int(input('Selecione o estado (1 a 4):\n1 - MG\n2 - SP\n3 - RJ\n4 - MS\n'))

if estado == 1:
    print(f'Valor final igual a {(valor * 0.07) + valor}')
if estado == 2:
    print(f'Valor final igual a {(valor * 0.12) + valor}')
if estado == 3:
    print(f'Valor final igual a {(valor * 0.15) + valor}')
if estado == 4:
    print(f'Valor final igual a {(valor * 0.08) + valor}')
