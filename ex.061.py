print('GERADOR DE PA...')
print('=' * 20)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} > '.format(termo), end='')
    termo += razão
    cont += 1
print('Fim')