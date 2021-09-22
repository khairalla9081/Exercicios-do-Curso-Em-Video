#salário = float(input('Qual o salário do funciodario? R$'))
#if salário >= 1250.00:
#    aumento = salário + (salário * 10 / 100)
#if salário <= 1250.00:
#    aumento = salário + (salário * 15 / 100)
#print('O salário de R${:.2f} agora com o aumento de 10% será R${:.2f}'.format(salário, aumento))

salário = float(input('Qual o salário do funciodario? R$'))
if salário <= 1250:
    aumento = salário + (salário * 15 / 100)
    print('O salário de R${:.2f} agora com o aumento de 15% será R${:.2f}'.format(salário, aumento))
else:
    aumento = salário + (salário * 10 / 100)
    print('O salário de R${:.2f} agora com o aumento de 10% será R${:.2f}'.format(salário, aumento))

