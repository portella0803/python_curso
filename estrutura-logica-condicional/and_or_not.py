"""
Estruturas Lógicas: and(e), or(ou), is(é)

Operadores unarios:
    - not, is
Operadores binários:
    - and, or

Regras de funcionamento:

Para o 'and', ambos valores precisan ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not, o valor do booleano é invertido, ou seja, se for True, vira False, se for False vira True
Para o 'is', o valor é comparado com um segundo
"""
ativo = False
logado = True

if ativo and logado:
    print('Bem-vindo Usuarios!')
else:
    print('Você previsa ativar sua conta, por favor cheque seu e-mail.')

if ativo or logado:
    print('Bem-vindo Usuarios!')
else:
    print('Você previsa ativar sua conta, por favor cheque seu e-mail.')


if not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo')


#Print (not False)
print(not True)
print(not False)


if ativo is True:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo')


#Ativo é Falso?
print(ativo is True)
