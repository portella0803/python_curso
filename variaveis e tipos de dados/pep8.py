"""
PEP8 - Python Enhancement Proposal

São propostas de melhoria para a línguagem Python

Zem of Python

import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica.

[1] - Utilize Camel Case para nomes de classes;

[2] - Utilize nomes em minúsculo, separados por underline para funções ou váriaveis;

[3] - Utilize 4 espaços para identação! (Não use tab)

[4] - Linhas em branco:
- Separar funções e definições de classe com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com um única linha em branco;

[5] - Imports:
- Imports devem ser sempre feitos em linhas separadas;
# Import Errado

import, sys, os

# Import Certo

import sys
import os

# Não há problemas em utilizar:

from trypes import StringType, ListType

# Caso tenha muitos imports de ums mesmo pacote, recomenda-se fazer:

from types import(
    Stringtype
    ListType
    SetType
    OutrosType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstring e antes de constantes ou variáveis globais.

[6] - Espaços em expressões e instruções:
# Não faça:

funcao( algo[ 1 ], { outro: 2 })

# Faça:

funcao(algo[1], {outro: 2})

# Não faça:

algo (1)

# Faça:

algo(1)

# Não faça:

dict ['chave'] = lista [indice]

# Faça:

dict['chave'] = lista[ídice]

# Não faça:

x             = 1
y             = 3
variavel_longa= 5

# Faça:

x = 1
y = 3
variavel_longa = 5

[7] - Termine sempre uma instrução com uma nova linha
"""
import this
