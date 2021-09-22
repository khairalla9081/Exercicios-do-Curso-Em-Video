#from random import choice
#num = int
#pc = choice([0, 1, 2, 3, 4, 5])
#user = int(input('Numero: '))
#if user == pc:
#    print('Você acertou!')
#else:
#    print('Você errou!')
#print('{}'.format(pc))

from random import randint
from time import sleep
computador = randint(0, 5) # Vai escolher um número
print('-=-' * 20)
print('Tente Adivinhar qual número que estou pensando de 0 A 5...')
print('-=-' * 20)
jogador = int(input('Qual número você acha que estou pensado? ')) # Vai tentar adivinhar o número
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('O número que eu pensei foi {}'.format(computador))
    print('Você ganhou de mim. Parabéns')
else:
    print('O número que eu pensei foi {}'.format(computador))
    print('GANHEI! DE você seu otario!!!!')

