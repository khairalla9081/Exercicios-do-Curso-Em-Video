print('\033[34m-=-\033[m' * 20)
print('\033[33mANALISADOR DE TRIANGULOS...\033[m')
print('\033[34m-=-\033[m' * 20)
r1 = float(input('PRIMEIRO segmento: '))
r2 = float(input('SEGUNDO segmento: '))
r3 = float(input('TERCEIRO segmento: '))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2: 
    print('Esses segmentos PODEM FORMAR um triangulo ', end='')
    if r1 == r2 == r3:
        print('do tipo \033[34mEQUILATERO\033[m')
    elif r1 != r2 != r3 != r1:
        print('do tipo \033[33mESCALENO\033[m')
    else:
        print('do tipo \033[31mISÓSELES\033[m')
else:
    print('Esses segmentos NÃO PODEM FORMAR um triangulo!')
