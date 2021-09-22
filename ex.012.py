produto = float(input('Qual é o preço do produto? R$'))
novo = produto - (produto * 5 / 100)
print('O produto que custava R${:.2f} agora com o desconto de 5% ele custara R${:.2f}'.format(produto, novo))