real = float(input('Quanto dinheiro você tem? R$'))
dolar = real / 5.22
euro = real / 6.35
print('Com tantos R${:.2f} você pode comprar US${:.2f} ou €{:.2f}'.format(real, dolar, euro))
