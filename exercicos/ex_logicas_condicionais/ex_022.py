idade = int(input('Qual sua idade?\n'))
tempo = int(input('Quantos anos você trabalhou?\n'))

if idade == 65 or tempo == 30:
    print('Pode se aposentar')
elif idade == 60 and tempo == 25:
    print('Pode se aposentar')
else:
    print('Não pode se aposentar')
