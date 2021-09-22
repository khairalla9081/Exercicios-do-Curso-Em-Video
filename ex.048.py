soma = 0
cont = 0
for c in range(1, 501, 2):
      if c % 3 == 0:
            cont += 1
            soma += c
print('A som a de todos os {} valores são {}'.format(cont, soma))
