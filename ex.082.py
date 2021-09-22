listNum = []
par = []
impar = []

while True:
    listNum.append(int(input('Digite um valor: ')))
    op = str(input('Quer continuar? [S/N] '))
    if op in 'Nn':
        break

for i, v in enumerate(listNum):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)

print(f'A lista completa é {listNum}')
print(f'A lista de pares é {par}')
print(f'A lista impares é {impar}')
