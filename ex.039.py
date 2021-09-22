from datetime import date
nome = str(input('Qual é o seu nome? ')).strip().title()
sexo = str(input('''Qual é o seu sexo? 
[ m ] Para Masculino
[ f ] Para feminino
Tecle em enter para continuar!'''))
opção = input('Seu sexo: ')
if opção == 'f':
    print('O alistamento não é obrigatorio para mulheres.')
    exit()
nasc = int(input('Qual é o ano do seu nascimento? '))
atual = date.today().year
idade = atual - nasc
print('{} tem {} anos em {}'.format(nome, idade, atual))
if idade == 18:
    print('{} você tem que se alistar IMEDIATAMENTE!'.format(nome))
elif idade < 18:
    saldo = 18 - idade
    print('{} seu alistamento sera daqui a {} anos'.format(nome, saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('{} você já deveria ter se alistado há {} anos!'.format(nome, saldo))
    ano = atual - saldo
    print('O seu alisatamento foi em {}'.format(ano))

