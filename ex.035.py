print('-=-' * 20)
print('Analisador de triangulo!')
print('-=-' * 20)
r1 = float(input('Qual é o segmento? '))
r2 = float(input('Qual é o segmento? '))
r3 = float(input('Qual é o segmento? '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Esses segmentos acima PODE FORMAR um triangulo!')
else:
    print('Esses segmentos NÃO PODEM FORMAR um treiangulo!')
