dados = []    
pessoas = {}
soma = media = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = ' '
    while pessoas['sexo'] not in 'MF':
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0] 
        if pessoas['sexo'] not in 'MF':
            print('ERRO! Por favor, digite apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    dados.append(pessoas.copy())
    pessoas.clear()

    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if op not in 'SN':
            print('ERRO! Responda apenas S ou N.')
    if op == 'N':
        break   
        
print('-=' * 40)
print(f'A) Ao todo temos {len(dados)} pessoas cadastradas.')

media = soma / len(dados)
print(f'A media do grupo é de {media:5.2f}')

print(f"C) As mulheres cadastrads foram ", end='')        
for i, v in enumerate(dados):
    if dados[i]['sexo'] == 'F':
        minas = dados[i]['nome']
        print(f'{minas}, ', end='')
print()

print('D) Lista de pessoas que estão acima da média:')
for i, v in enumerate(dados):
    if v['idade'] >= media:
        print(f'   nome = {v["nome"]}; sexo = {v["sexo"]}; idade = {v["idade"]}')    
