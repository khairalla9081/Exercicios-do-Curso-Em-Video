"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e 
cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, 
o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, 
com quantos anos a pessoa vai se aposentar.
"""
from datetime import date 

dados = {}

dados['nome'] = str(input('Nome: '))
nasc= int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

#atual = date.today().year
dados['idade'] = date.today().year - nasc

# if dados['ctps'] == 0:
#     print('-=' * 40)
#     print(f'nome tem o valor {dados["nome"]}')
#     print(f'Idade tem o valor {idade}')
#     print(f'ctps tem o valor {dados["ctps"]}')

if dados['ctps'] != 0:   
    dados['contrato'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: '))
    posent = dados['contrato'] + 35
    dados['posent'] = posent - dados['idade']

print('-=' * 30)

for k, v in dados.items():
    print(f'- {k} tem o valor {v}')

    # print('-=' * 40)
    # print(f'nome tem o valor {dados["nome"]}')
    # print(f'Idade tem o valor {idade}')
    # print(f'ctps tem o valor {dados["ctps"]}')
    # print(f'Contrato tem o valor {dados["contrato"]}')
    # print(f'Salário tem o valor {dados["salario"]}')
    # print(f'Aposetadoria tem o valor {dados["posent"]}')
