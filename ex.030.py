número = int(input('Digite um número para ver se ele é PAR ou IMPAR: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é PAR'.format(número))
else:
    print('O número {} é IMPAR'.format(número))
