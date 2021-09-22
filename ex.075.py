num = (int(input('Digite um numero: ')), int(input('Digite um numero: ')),
       int(input('Digite um numero: ')), int(input('Digite um numero: ')))

print(f'O numero 9 foi digitado {num.count(9)} vezes')

if num == 3:
       print(f'O numero 3 está na {num.index(3)+1} posição')
else:
       print(f'O numero 3 não foi digitado.')

print(f'Os numeros PARES que foram digitados foram:', end='')
for n in num:
       if n % 2 == 0:
              print(f'{n},', end='')
       else:
              print('Nem um numero PAR foi digitado.')
