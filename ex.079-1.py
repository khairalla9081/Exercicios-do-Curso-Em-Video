list_number = []

while True:
    n = int(input('Digite um valor: '))
    if n not in list_number:
        print('Valor adicionado...')
        list_number.append(n)
    else:
        print('Valor duplicado, não foi adicionado...')
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break

list_number.sort()
print(list_number)
