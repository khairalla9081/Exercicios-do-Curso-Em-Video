peso = float(input('Seu peso:(kg) '))
altura = float(input('Sua altura:(m) '))
imc = peso / (altura ** 2 )
print('O imc dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
      print('Seu IMC é {:.1f} está ABAIXO DO PESO normal, CUIDADO!'.format(imc))
elif 18.5 <= imc < 25:
      print('Seu IMC é {:.1f} está no PESO NORMAL!'.format(imc))
elif 25 <= imc < 30:
      print('Seu IMC é {:.1f} está no NIVEL SOBREPESO!'.format(imc))
elif 30 <= imc < 40: 
      print('Seu IMC é {:.1f} está no NIVEL OBESIDADE!'.format(imc))
elif imc >= 40:
      print('CUIDADO seu IMC é {:.1f} está no NIVEL OBESIDADE MÓRBIDA!'.format(imc))
