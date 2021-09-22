nota_1 = float(input('Qual foi sua PRIMEIRA nota? '))
nota_2 = float(input('Qual foi sua SEGUNDA nota? '))
média = (nota_1 + nota_2) / 2
print('A média foi {:.1f}'.format(média))
if média < 5:
    print('\033[31mREPROVADO, estude mais da proxima!\033[m')
elif média <= 6.9:
    print('\033[33mVocê está de RECUOERAÇÃO!\033[m')
elif média > 7:
    print('\033[32mPARABENS, você foi APAROVADO!\033[m')
