from datetime import date
ano = int(input('Qual ano você quer analizar? Cloque 0 para ver o ano atual:  '))  # O usuario vai digitar o ano!
if ano == 0:                                                                       # Aqui o Programa vai me mostrar o ano atual.
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:                              # Aqui vai me dizer se ele é BISSEXTO!
    print('O ano {} é BISSEXTO!'.format(ano))
else:                                                                              # E aqui vai me dizer se o ano não é BISSEXTO!
    print('O ano {} NÃO é BISSEXTO!'.format(ano))
