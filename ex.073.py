times = ('Flamengo', 'Internacional', 'Atlético', 'São Paulo',
         'Fluminense', 'Grêmio', 'Palmeiras', 'Santos',
         'Athletico Paranaense', 'Red Bull Bragantino',
         'Ceará', 'Corinthians', 'Atlético', 'Bahia',
         'Sport', 'Fortaleza', 'Vasco da Gama',
         'Goiás', 'Coritiba', 'Botafogo')

print(f'Os 5 Primeiros times da Tabela do Campeonato Brasileiro \033[31m{times[:5]}\033[m')
print(f'Os 4 Ultimos Colocados da Tabela do Campeonato Brasileiro \033[31m{times[-4:]}\033[m')
print(f'Os times em ordem alfabetica ficara \033[31m{sorted(times)}\033[m')
print(f'O Corinthians está na posição \033[31m{times.index("Corinthians")+1}\033[m')
