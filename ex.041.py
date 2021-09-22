from datetime import date
atual = date.today().year
nome = str(input('Qual é o seu nome completo? '))
ano = int(input('Ano de nascimento: '))
idade = atual - ano
print('{} tem {} anos sua '.format(nome, idade), end='')
if idade <= 9:
    print('categoria é: MIRIM')
elif idade <= 14:
    print('categoria é: INFANTIL')
elif idade <= 19:
    print('categoria é: JÚNIOR')
elif idade <= 25:
    print('categoria é: SÊNIOR')
elif idade > 25:
    print('categoria é: MASTER')
 