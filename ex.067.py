tab = 1
cont = 1
while True:
    print('-' * 40)
    tab = int(input('Quer ver a tabuada de que número? '))
    print('-' * 40)
    if tab < 0:
        break
    for cont in range(1, 11):
        soma = tab * cont
        print(f'{tab} X {cont} = {soma}')
print('PROGRAMA DE TABUDADA FINALIZADO. Volte sempre!')
