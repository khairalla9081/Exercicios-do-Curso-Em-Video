# Meu programa
# def ficha(name=False, gols=False):
#     if name == '':
#         name = '<desconhecido>'
#     elif gols == '':
#         gols = 0
#     print(f'O jogador {name} fez {gols} gol(s).')


# nome = str(input('Nome do jogador: '))
# gol = str(input('Número de gols: '))
# ficha(nome, gol)
# --------------------------------------------------
# Programa do Guanabara
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input("Nome do jogador: "))
g = str(input("Número de gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
