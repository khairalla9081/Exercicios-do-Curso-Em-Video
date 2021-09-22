sexo = str(input('Informe seu sexe [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos! Por favor informe seu sexo [M/F]: ')).strip().upper()[0]  
print('Sexo {} resgistrado com sucesso!'.format(sexo))