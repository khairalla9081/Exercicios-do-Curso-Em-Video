"""
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.
"""

aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situa'] = 'Aprovado'
elif aluno['media'] <= 5:
    aluno['situa'] = 'Reprovado'
else:
    aluno['situa'] = 'Recuperação'

print('-=' * 40)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
# print(aluno)
# print(f'- nome é igual a {aluno["nome"]}')
# print(f'- média é igual a {aluno["media"]}')
# print(f'- situação é igual a {aluno["situa"]}')
