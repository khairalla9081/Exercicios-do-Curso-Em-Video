from math import radians, cos, sin, tan
an = float(input('Digite p âgulo que você deseja: '))
sen = sin(radians(an))
print('O angulo de {} tem o SENO de {:.2f}'.format(an, sen))
cos = cos(radians(an))
print('O angulo de {} tem o SENO de {:.2f}'.format(an, cos))
tan = tan(radians(an))
print('O angulo de {} tem o TANGENTE de {:.2f}'.format(an, tan))