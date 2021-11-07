#>>>>>> MODO SIMPLES USANDO UM MODULO
#from math import factorial
#n = int(input('Digite um número para calcular o seu fatorial: '))
#f = factorial(n)
#print('O fatoria de {} é {}.'.format(n, f))

#>>>>> USANDO O WHILE
#n = int(input('Digite um número para calcular o seu fatorial: '))
#c = n
#f = 1
#print('Calculando o {}! = '.format(n), end='')
#while c  > 0:
#    print('{}'.format(c), end='')
#    print(' x ' if c > 1 else ' = ', end='')
#    f *= c
#    c -= 1
#print('{}'.format(f))

#>>>> USANDOP O FOR!
n = int(input('Digite um número para calcular o seu fatorial: '))
c = n
f = 1
print('Calculando o {}! = '.format(n), end='')
for c in range(n, 0, -1):
   f *= c
   print('{}'.format(c), end='')
   print(' X ' if c > 1 else ' = ', end='')
print('{}'.format(f))
