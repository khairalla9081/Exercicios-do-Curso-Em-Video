# pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':19}
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

# pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':19}
# print(pessoas.keys()) ## >>> dict_keys(['nome', 'sexo', 'idade'])

# pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':19}
# print(pessoas.values()) ## >>> dict_values(['Gustavo', 'M', 19])

# pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':19}
# print(pessoas.items()) ## >>> dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 19)])

# pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':19}
# pessoas['peso'] = 80.3
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# brasil = []
# estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
# estado2 = {'uf':'São Paulo', 'sigla':'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil[1]['sigla'])

# estado = dict()
# brasil = list()

# for c in range(0, 3):
#     estado['uf'] = str(input('Unidade Federativa: '))
#     estado['sigla'] = str(input('Sigla do estado: '))
#     brasil.append(estado.copy())

# for e in brasil:
#     for k, v in e.items():
#         print(f'O campo {k} tem o valor {v}')