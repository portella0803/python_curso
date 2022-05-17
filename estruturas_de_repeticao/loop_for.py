"""
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas

C ou Java

for(int i = 0; i<10; i++){
    //execução do loop
}

Python

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome =  geek university
- Listas
    lista = [1, 2, 3,4]
-Range:
    numeros = range(1, 16)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que tranformar numa lista

#Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

#Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

#Exemplo de for 3 (Iterando sobre um range)

Range (valor_inicial, valor_final)

OBS: O valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - não

for numero in range (1,10):
    print(numero)

#enumerate
for indice, v  in enumerate(nome):
    print(nome[indice])

for _, letra in enumerate(nome):
    print(letra)
OBS: Quando precisamos de um valor, podemos descarta-lo utilizando um underline (_)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que tranformar numa lista

for valor in enumerate(nome):
    print(valor)

#outro exemplo com somas:

qtd = int(input("Quantas vezes esse loop deve rodar? \n"))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

#exemplo 
nome = 'geek university'
for letra in nome:
    print(letra, end='')

Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode

"""

#Original: U+F60D
#Modificado: U000F60D

for num in range (1, 11):
    print('\U000F60D' * num)
