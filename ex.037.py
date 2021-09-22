num = int(input('Digite um número: '))
print('''Esconha um número para ver para ver a sua conversão: 
[ 1 ] converter para Binario
[ 2 ] concerter para Octal
[ 3 ] converter para Hexadecimal''')
opção = int(input('Digite sua opção: '))
if opção == 1:
    print('O número {} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O número {} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O número {} convertido para HESXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida. Tente novamente!')