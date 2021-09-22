print('{:=^40}'.format(' LOJAS KHAIRALLA '))
preço = float(input('Preço da compras: R$ '))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''')
opção = int(input('Qual é a opção: '))
if opção == 1:
      total= preço - (preço * 10 / 100)
elif opção == 2:
      total = preço - (preço * 5 / 100)  
elif opção == 3:
      total = preço
      parcela = total / 2
      print('sua compra será parcelada 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4: # fiquei bugado nesse ultimo elif
      total = preço + (preço * 20 / 100)
      totparc = int(input('Em quantas parcelas: '))
      parcela = total / totparc
      print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
      print('OPÇÃO INVALIDA, tente novamente...')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
