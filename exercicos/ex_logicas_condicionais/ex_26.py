km = float(input('Quantos quilometros foram pecorridos?\n'))
litros = float(input('Quantos litros gastos?\n'))

kml = km / litros

if kml < 8:
    print(f'{kml}Km/l')
    print('Venda o carro!')
elif kml > 12:
    print(f'{kml}Km/l')
    print('Super econômico!')
else:
    print(f'{kml}Km/l')
    print('Econômico!')
