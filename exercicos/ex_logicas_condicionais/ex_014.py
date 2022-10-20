n1 = float(input('Digite a nota do Trabalho de Laboratório:\n'))
n2 = float(input('Digite a nota da Avaliação Semestral:\n'))
n3 = float(input('Digite a nota do Exame Final:\n'))

media = (n1 * 2 + n2 * 3 + n3 * 5) / 10

if media <= 2.9:
    print(f'Aluno Reprovado! Media igual a {media}')
elif media <= 4.9:
    print(f'Aluno em Recuperação! Media igual a {media}')
else:
    print(f'Aluno Aprovado! Media igual a {media}')
