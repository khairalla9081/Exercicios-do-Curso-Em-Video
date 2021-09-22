from random import randint
jogos = []
senajogos = []

print('-=' * 20)
print('         JOGO NA MEGA SENA       ')
print('-=' * 20)

jogador = int(input('Quantos jogos você deseja fazer: '))
tot = 1
while tot <= jogador:
    cont = 0
    while True:  
        sortenum = randint(1, 60)
        if sortenum not in jogos:
            jogos.append(sortenum)
            cont += 1
        if cont >= 6:
            break
    jogos.sort()
    senajogos.append(jogos[:])
    jogos.clear()
    tot += 1
for i, l in enumerate(senajogos):
    print(f'jogo {i+1}: {l}')