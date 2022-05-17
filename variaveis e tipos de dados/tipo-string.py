"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples -> 'uma string', '234', 'a', 'true', '42.3
- Estiver entre aspas duplas -> "uma string", "234", "a", "true", "42.3"
- Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''true''', '''42.3'''

"""
# Estiver entre aspas duplas triplas -> """uma string""", """234""", """a""", """true""", """42.3"""

#Exemplos de string para mostrar o type
"""
nome = 'geek'
print(nome)
print(type(nome))

nome = "Gina`s Bar"
print(nome)
print(type(nome))

nome = '''Angelina \nJolie'''
print(nome)
print(type(nome))
"""
#nome = """Angelina Jolie"""
#print(nome)
#print(type(nome))

#Tudo Maiusculo
nome = 'geek'
print(nome.upper())

#Tudo Minusculo
nome = 'GEEK'
print(nome.lower())

#Transforma em uma lista de strings
nome = 'Geek University'
print(nome.split())

#É possivel printar só uma parte da string ja que cada coisa digitada numa string se tranforma num vetor
# [ 0 , 1 ,  2 ,  3]
# ['g','e', 'e', 'k',]
nome = 'geek'
print(nome[0:2]) #slice de string
print(nome[0:3]) #slice de string

# [0, 1]
#'geek', 'university'
nome = 'geek university'
print(nome.split()[0])

print(nome.split()[1])

#Comece no primeiro elemento, vá até o ultimo e inverta
print(nome[::-1]) #inversão da string

print(nome.replace('g', 'p')) #Altera um vetor por outro

#Palindromo
texto = 'socorram me subino onibus em marrocos'
print(texto)

print(texto[::-1])
