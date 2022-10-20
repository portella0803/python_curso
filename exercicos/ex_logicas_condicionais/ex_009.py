salario = float(input('Digite o valor do seu salário:\n'))
parcela = float(input('Digite os valor das parcelas:\n'))

if (salario * 0.20) > parcela:
    print('Empréstimo concedido!')
else:
    print('Empréstimo não concedido!')
