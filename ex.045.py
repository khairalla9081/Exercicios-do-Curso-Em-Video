from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print('''SUAS OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 12)
print('O computador jogou: \033[34m{}\033[m'.format(itens[pc]))
print('O jogador jogou: \033[31m{}\033[m'.format(itens[jogador]))
print('-=' * 12)
if pc == 0: 
      if jogador == 0: # pedra
            print('\033[31m<<< EMPATE >>>\033[m')
      elif jogador == 1:
            print('JOGADOR GANHOU!!')
      elif jogador == 2:
            print('COMPUTADOR GANHOU!!')
      else:
            print('\033[31mJOGADA INVALIDA\033[m')
elif pc == 1: # papel
      if jogador == 1:
            print('\033[31m<<< EMPATE >>>\033[m')
      elif jogador == 2:
            print('JOGADOR GANHOU!!')
      elif jogador == 0:
            print('COMPUTADOR GANHOU!!')
      else:
            print('\033[31mJOGADA INVALIDA\033[m')
elif pc == 2: # tesoura
      if jogador == 2:
            print('\033[31m<<< EMPATE >>>\033[m')
      elif jogador == 0:
            print('JOGADOR GANHOU!!')
      elif jogador == 1:
            print('COMPUTADOR GANHOU!!')
      else:
            print('\033[31mJOGADA INVALIDA\033[m')
