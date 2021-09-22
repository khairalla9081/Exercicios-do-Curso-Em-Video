total = cont1000 = menor = cont = 0
cheapest = ''
while True:
    name_product = str(input('Name of the product: ')).strip()
    price_product = float(input('Price of the product US$: '))
    cont += 1
    total += price_product
    if price_product >= 1000:
        cont1000 += 1
    if cont == 1:
        menor = price_product
        cheapest = name_product
    else:
        if price_product < menor:
            menor < price_product
            cheapest = name_product

    option = ' '
    while option not in 'YN':
        option = str(input('Do you would like to continue [Y/N] YES or NOT? ')).strip().upper()[0]
    if option == 'N':
        break

print(f'the total purchase was {total}')
print(f'We have {cont1000} products costing over US$ 1000')
print(f'The cheapest product was a {cheapest} that costs {menor}')
