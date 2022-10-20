opcao = int(input('Digite a opção que deseja (1 à 2):\n1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\n'))

if opcao == 1:
    n1 = float(input('Digite um número:\n'))
    n2 = float(input('Digite um outro número:\n'))
    print(f'A soma dos valores é igual a {n1 + n2}')
elif opcao == 2:
    n1 = float(input('Digite um número:\n'))
    n2 = float(input('Digite um outro número:\n'))
    print(f'A subtração dos valores é igual a {n1 - n2}')
elif opcao == 3:
    n1 = float(input('Digite um número:\n'))
    n2 = float(input('Digite um outro número:\n'))
    print(f'A multiplicação dos valores é igual a {n1 * n2}')
elif opcao == 4:
    n1 = float(input('Digite um número:\n'))
    n2 = float(input('Digite um outro número:\n'))
    print(f'A divisão dos valores é igual a {n1 / n2}')
else:
    print('[ERRO] - Opção Inválida')
