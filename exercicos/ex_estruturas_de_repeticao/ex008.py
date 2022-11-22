valor = int(input('Digite um valor inteiro:\n'))
for i in range(10):
    valor += 1
    if valor % 2 != 0:
        print(valor)
    