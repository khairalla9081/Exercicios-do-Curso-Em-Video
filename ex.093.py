"""My code"""
dados = {}
gols = []

dados['nome'] = str(input('Nome do jogador: '))
partida = int(input(f'Quantas partidas {dados["nome"]} jogou? ')) 

for c in range(partida):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
    dados['gols'] = gols
    dados['total']= 0
    for i in gols:
        dados['total'] += i

print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)

print(f'O jogador {dados["nome"]} jogou {partida} partidas.')
cont = 0
for v in dados['gols']:
    print(f'--> Na partida {cont}, fez {v} gols.')
    cont += 1
print(f'Foi um total de {dados["total"]} gols.')

# """Guanabara's code"""
# jogador = dict()
# partidas = list()

# jogador['nome'] = str(input('Nome do jogador: '))
# tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
# for c in range(0, tot):
#     partidas.append(int(input(f'Quantos gols na partida {c}? ')))
# jogador['gols'] = partidas[:]
# jogador['total'] = sum(partidas)

# print('-=' * 30)
# print(jogador)
# print('-=' * 30)

# for k, v in jogador.items():
#     print(f'O campo {k} tem o valor {v}')
# print('-=' * 30)

# print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
# for i, v in enumerate(jogador['gols']):
#     print(f'--> Na partida {i}, fez {v} gols.')
# print(f'Foi um total de {jogador["total"]} gols.')