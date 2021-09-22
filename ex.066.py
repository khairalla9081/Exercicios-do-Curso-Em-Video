cont = 0
s = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'E a soma de {cont} valor foi de {s}.')
