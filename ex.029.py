velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO!! VOCÊ ULTRAPASSOU O LIMITE DE VELOCIDADE PERMITIDO QUE É 80KM/H')
    multa = (velocidade - 80) * 7 # conta da multa!
    print('A MULTA QUE TERÁ QUE PAGAR VAI SER R${:.2f}'.format(multa))
print('Dirija com cuidado!')
