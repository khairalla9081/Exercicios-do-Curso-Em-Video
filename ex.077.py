palavras = ('DIGNIDADE', 'ESPALHAFATOSA',
            'COBRANÇA', 'AGRECIVIDADE',
            'CRITERIO', 'PORTA')

for p in palavras:
    print(f'\nNa palavra \033[31m{p}\033[m temos', end=' ')
    for v in p:
        if v.lower() in 'aeiou':
            print(v, end=' ')