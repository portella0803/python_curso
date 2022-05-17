"""
Escopo de variaveis

Dois casos de escopo:

1- Variaveis globais;
    - Variaveis globais são reconhecidas, ou seja, 
    seu corpo compreende, todo o programa

2- Variaveis locais;
    - Variaveis locais são reconhecidas apenas no bloco onde 
    foram declaradas, ou seja, seu escopo está limitado ao bloco onde foi declarada.

Para declarar variaveis em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é um linguagem de tipagem dinamica. Isso significa que ao declararmos
uma variavel, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor a mesma.

"""

numero = 42 #exemplo de variavel global
print(numero)
print(type(numero))

numero = 'geek'
print(numero)
print(type(numero))

nao_existo = 'Oi'
print(nao_existo)

numero = 42

if numero > 10:
    novo = numero + 10 #a variavel novo esta declarada localmente dentro do bloco if. Portanto novo é local
    print (novo)