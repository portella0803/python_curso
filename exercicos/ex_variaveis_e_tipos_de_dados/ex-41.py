v = float(input('Digite o valor da hora de trabalho:\n'))
h = int(input('Quantas horas foram trabalhadas?\n')) * v

print(f'O funcionario ira receber R$ {(h * 0.10) + h}')
