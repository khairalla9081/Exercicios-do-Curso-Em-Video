resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: '))
média = soma / quant
print('Você digitou {} números e média deles foi {}'.format(quant, média))
print('O maior número digitado foi {} e o menor foi {}!'.format(maior, menor))
