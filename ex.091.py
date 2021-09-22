"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário
em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from time import sleep
#from operator import itemgetter

jogo = {'jogador-1':randint(1, 6), 
        'jogador-2':randint(1, 6), 
        'jogador-3':randint(1, 6), 
        'jogador-4':randint(1, 6) 
        }
# ranking = {} # or []

print('\33[31mQue joguem os dados...\033[m')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-=' * 30)

c = 1
jogo2 = dict(sorted(jogo.items(), key=lambda x:x[1], reverse=True))
# ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for k, v in jogo2.items():
    print(f'{c} lugar: {k} com {v}')
    c +=1
    sleep(1)
