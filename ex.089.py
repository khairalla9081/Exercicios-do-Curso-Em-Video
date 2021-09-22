"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário 
possa mostrar as notas de cada aluno individualmente.
"""

boletin = []

while True:

    nome = str(input('Nome: '))
    n1 = float(input('Nota 1:'))
    n2 = float(input('Nota 2:'))
    media = (n1 + n2) / 2
    boletin.append([nome, [n1, n2], media])
    
    op = ' '
    while op not in 'SnNn':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break

print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
for i, a in enumerate(boletin):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')

while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(boletin) - 1:
        print(f'Notas de {boletin[opc][0]} são {boletin[opc][1]}')
print('FIM.')