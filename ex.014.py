c = float(input('Qual é a temperatura? '))
f = (c * 9 / 5) + 32
print('A temperatura de {:.1f}°C corresponde a {:.1f}°F'.format(c, f))
#((9*c)/5) +32

f = float(input('Qual é a temperatura? '))
c = (f - 32) * 5 / 9
print('A temperatura de {:.1f}°F corresponde a {:.1f}°C'.format(f, c))
