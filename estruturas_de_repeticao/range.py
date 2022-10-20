"""
Ranges

- Precisamos conhecer o loop para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequencias numericas, não de forma aleatoria, mas sim maneira especifica.

Formas gerais:

range(valor_de_parada)

OBS: valor_de_parada não inclusive (inicio padrão 0, e passo de 1 em 1)

# forma 1
for num in range(11):
    print(num)

# forma 2
range(valor_de_inicio, valor_de_parada)
OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo de 1 em 1)
for num in range(1, 11):
    print(num)

# forma 3
range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (inicio especificado pelo usuario, e passo especificado pelo usuario)
for num in range(1, 10, 2)
    print(num)

# forma 4 (inversa)
range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (inicio especificado pelo usuario, e passo especificado pelo usuario)
for num in range (10, 0, -1):
    print(num)
"""
