"""
Listas

Listas em Python funcional como vetores/matrizes (arrays) em outras linguagens, com a
diferença de serem DINÂMICO e também de podermos colocar QUALQUER tipode de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um arrray do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Python:

- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplismente ir adicionado elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado.

As listas em Python são representadas por colchetes: []
"""
type([])

lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = ['U', 'n', 'i', 'v', 'e', 'r', 's', 'o']
lista3 = []
lista4 = list(range(11))
lista5 = list('Universo')
# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados
lista6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 123456789]
print(lista1, lista2, lista3, lista4, lista5, lista6)

# Podemos facilmente checar se determinado valor está contido na lista
if 8 in lista4:
    print('Encontrei o número 8')
else:
    print('Não encontrei  número 8')

# Podemos facilmente ordenar uma lista
print(lista1.sort())

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas

"""
Para adicionar elementos em listas, utilizamos a função append

OBS: Com append, nós só conseguimos adicionar 1 elemento por vez
"""
print(lista1)
lista1.append(42)
print(lista2)

# lista1.append(12, 34, 56) #ERRO

lista1.append([8, 9, 10]) # Coloca a lista como elemento único (sublista)
print(lista1)

if [8, 9 ,10] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67]) #Coloca cada elemento da lista como valor adicional à lista
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
# OBS: Isso não substitui o valor inicial. O mesmo será deslocado para direita da lista
lista1.insert(2, 'Novo Valor')
print(lista1)

# Podemos facilmente juntar duas listas

lista6 = lista1 + lista2
# lista1. extend(lista2)
print(lista6)

#POdemos facilemente inverter uma lista

# Forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Forma 2
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista

lista6 = lista2.copy()
print(lista6)

# Para saber o tamnho de uma lista

print(len(lista1))

# Podemos facilmente remover o último elemento de uma lista
# OBS: O pop não somente remove o último elemento como também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
# OBS: Os elementos à direita deste índice serão deslocados para esquerda
# OBS: Se não houver elemento no índice informaado, teremos o erro IndexError
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista

# Exemplo 1

curso = 'Porgramação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas

# Exemplo 2
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string

lista6 = ['Programação', 'em', 'Python', 'Essencial']
print(lista6)
# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# Iterando sobre listas

# Exemplo 1

# soma = 0
# for elemento in lista1:
#     print(elemento)
#     soma = soma + elemento
# print(soma)

# Exemplo 2 - Utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elemntos de forma indexada

#           0          1        2        3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) # verde
print(cores[1]) # amarelo
print(cores[2]) # azul
print(cores[3]) # branco

# fazer acesso aos elementos de forma indexada inversa

print(cores[-4]) # verde
print(cores[-3]) # amarelo
print(cores[-2]) # azul
print(cores[-1]) # branco

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)

# Outros métodos não tão importantes mas também úteis

# Encontrar o índice de um lemento na lista

numeros =[5, 6, 7, 5, 8, 9, 10]

# Em qual índice está o valor 6?
print(numeros.index(6))
# Em qual índice está o valor 9?
print(numeros.index(9))

# OBS: Caso não tenha este lemento na lista, será apresentado erro ValueError

print(numeros.index(5)) # Retorna o índece do primeir elemento encontrado

# Podemos fazer busca dentro de um range, ou seja, qual índece começar a buscar
print(numeros.index(5, 1)) # Buscando a partir do índice 1

# Podemos fazer busca dentro de um range, ínicio/fim
print(numeros.index(8, 3, 6)) # Buscamos o índice do valor 8, entre os índices 3 a 6

# Revisão de slicing
# lista[inicio:fim:passo]
# range(inicio:fim:passe)

# Trabalhando com slice de lista com o parâmetro 'início'

lista = [1, 2, 3, 4]
print(lista[1:]) # Iniciando no índice 1 e pegando todos os elemntos restantes

# Invertendo valores em uma lista
nome = ['geek', 'university']

nome[0], nome[1] = nome[1], nome[0]
print(nome)

nomes = ['geek', 'university']
nomes.reverse()
print(nomes)

# Soma, valor máximo, valor mínimo, tamanho

# Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  # soma
print(max(lista))  # máximo valor
print(min(lista))  # mínimo valor
print(len(lista))  # tamanho da lista e funciona em qualquer tipo de dado

# Transformaar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Dsempacotamentode listas

lista = [1, 2, 3]
num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# OBS: Se tivermos um número diferente de elemntos na lista ou variáveis para receber os dados, teremos ValueError

# Copiando u lista para outra (Shallow Copy e Deep Copy)

# Forma 1

lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)
print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy copiamos dados da lista parra uma nova lista, mas elas totalmente indepedentes,
# ou seja, modificando uma lista, não afeta a outra. Isso em Python é chamado de DEep COpy (cópia profunda)

#Forma 2 - Shallow Copy
lista = [1, 2, 3]
print(lista)

nova = lista  #cópia
print(nova)

nova.append(4)
print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas
# após realizar modificação em uma listas, essa modificação se refletiu em ambas as listas. Isso em Python é
# chamado de Shallow Copy.
