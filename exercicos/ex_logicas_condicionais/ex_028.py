import random

# Gerando números aleatorios
n1 = random.randrange(1,100)
n2 = random.randrange(1,100)
n3 = random.randrange(1,100)
n4 = random.randrange(1,100)
n5 = random.randrange(1,100)
n6 = random.randrange(1,100)
n7 = random.randrange(1,100)
n8 = random.randrange(1,100)
n9 = random.randrange(1,100)
n10 = random.randrange(1,100)

# Somando eles
soma1 = n1 + n2
soma2 = n3 + n4
soma3 = n5 + n6
soma4 = n7 + n8
soma5 = n9 + n10

# Fazendo perguntas e verficando as respostas
# Pergunta 1
p1 = int(input(f'Quanto é {n1} + {n2}?\n'))
if soma1 == p1:
    print(f'Parabens você acertou, a resposta é {soma1}\n')
else:
    print('Você errou mas continue estudando')
    print(f'A resposta correta é {soma1}\n')
# Pergunta 2
p2 = int(input(f'Quanto é {n3} + {n4}?\n'))
if soma2 == p2:
    print(f'Parabens você acertou, a resposta é {soma2}\n')
else:
    print('Você errou mas continue estudando')
    print(f'A resposta correta é {soma2}\n')
# Pergunta 3
p3 = int(input(f'Quanto é {n5} + {n6}?\n'))
if soma3 == p3:
    print(f'Parabens você acertou, a resposta é {soma3}\n')
else:
    print('Você errou mas continue estudando')
    print(f'A resposta correta é {soma3}\n')
# Pergunta 4
p4 = int(input(f'Quanto é {n7} + {n8}?\n'))
if soma4 == p4:
    print(f'Parabens você acertou, a resposta é {soma4}\n')
else:
    print('Você errou mas continue estudando')
    print(f'A resposta correta é {soma4}\n')
# Pergunta 5
p5 = int(input(f'Quanto é {n9} + {n10}?\n'))
if soma5 == p5:
    print(f'Parabens você acertou, a resposta é {soma5}\n')
else:
    print('Você errou mas continue estudando')
    print(f'A resposta correta é {soma5}\n')
