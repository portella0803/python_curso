n1 = float(input('Digite a nota do aluno:\n'))
n2 = float(input('Digite a nota do aluno:\n'))
n3 = float(input('Digite a nota do aluno:\n'))

media = (n1 * 1 + n2 * 1 + n3 * 2) / 5

if media >= 60:
    print(f'Aluno Aprovado! Média igual a {media}')
else:
    print(f'Aluno Reprovado! Média igual a {media}')
