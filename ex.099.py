from random import randint
from time import sleep

def maior():
    listnum = []
    print('Analisando os valores passados...')

    for i in range(0, 5):
        num = randint(0, 10)
        if num not in listnum:
            listnum.append(num)
    
    print(f'{listnum} Foram informados {len(listnum)} valores ao todo.')
    print(f'O maior valor informado foi {max(listnum)}')

# Programa pricipal
for i in range(0, 4):
    maior()
    sleep(0.5)
    print('--' * 30)


# def maior(*num):
#     cont = maior = 0
#     print('Analisando os valores passados...')
#     for i in num:
#         print(f'{i} ', end='', flush=True)
#         sleep(0.5)
#         if cont == 0:
#             maior = i
#         else:
#             if i > maior:
#                 maior = i
#         cont += 1
#     print(f'Foram informados {cont} valores ao todo.')
#     print(f'O maior numero informado foi {maior}')
#     print('--' * 30)


# maior(7, 4, 2, 82)
# maior(8, 3, 22)