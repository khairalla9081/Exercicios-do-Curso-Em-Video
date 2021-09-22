listNum = []

while True:
    num = int(input('Digite um valor: ').strip())
    if num not in listNum:
        listNum.append(num)
    
    op = ' '
    while op not in 'SN':
        op = str(input('Voce quer continuar [S/N]? ')).upper()
    if op == 'N':
        break

print(sorted(listNum))
