salario = float(input('Qual é o seu salario do funcionario? R$'))
novo = salario + (salario * 15 / 100)
print('O salario que era {:.2f} agora com o será {:.2f}'.format(salario, novo))
