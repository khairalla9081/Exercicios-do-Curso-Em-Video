distacia = float(input('Qual é a distância da sua viagem? '))
print('Sua viagem de {}km já vai começar!'.format(distacia))
if distacia <= 200:
    preço = distacia * 0.50
else:
    preço = distacia * 0.45
print('Sua viagem vai custar R${:.2f}'.format(preço))

#distancia = float(input('Qual é a distancia de sua viagem? '))
#print('Você está preste a começar uma viagem de {}km'.format(distancia))
#preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
#print('E o preço da sua viagem será de R${:.#2f}'.format(preço))