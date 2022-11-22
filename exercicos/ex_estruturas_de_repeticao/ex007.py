
for n in range(1, 10):
    num = 0
    guardar_maior = num
    guardar_menor = num

    num = float(input(f'Digite o valor de {n}: '))

    if num > guardar_maior:
        guardar_maior = num
    elif num < guardar_menor:
        num = guardar_menor

    print(f'{guardar_maior}, {guardar_menor}')
