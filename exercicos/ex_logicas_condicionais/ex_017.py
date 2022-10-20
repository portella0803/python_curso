maior = float(input('Digite a base maior:\n'))
menor = float(input('Digite a base menor:\n'))
h = float(input('Digite a altura:\n'))

if maior > 0 and menor > 0:
    a = ((maior + menor) * h) / 2
    print(f'A área do trapézio é igual a {a}')
else:
    print('[ERRO] - Valor das Bases Inválidos!')
