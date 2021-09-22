## Meu codigo.
# --------------------------------------------------------

listaNum = []
cont = 0

while True:
    num = int(input('Digite um valor: '))
    listaNum.append(num)
    cont += 1

    op = ' '
    while op not in 'SN':
        op = str(input('Voce quer continuar [S/N]? ')).upper().strip()[0]
    if op == 'N':
        break

print('--' * 40)
print(f'Lista: {listaNum}')
print(f'Foram adicionados {cont} valores na lista...')
listaNum.sort(reverse=True)
print(f'A lista ordenada{listaNum}')

if 5 in listaNum:
    print('O numero 5 FOI digitado na lista.')
else:
    print('o numero 5 NAO FOI digitado na lista.')

## Codigo do Guanabara.
# --------------------------------------------------------

valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print('-=' * 40)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')

if 5 in listaNum:
    print('O numero 5 FOI digitado na lista.')
else:
    print('o numero 5 NAO FOI digitado na lista.')
