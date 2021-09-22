#num = 0
#cont = 0
#soma = 0
#while num != 999:
#    num = int(input('Digite um número [999 para parar]: '))
#    cont += 1
#    soma += num
#print('Você digitou {} números, e soma entre eles foi {}'.format(cont - 1, soma - 999))

num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números, e soma entre eles foi {}'.format(cont, soma))
