dias = int(input('quantos dias alugados? '))
km = float(input('Quantos quilometros rodados? '))
total = (dias * 60.00) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(total))