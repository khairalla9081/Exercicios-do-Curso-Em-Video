dados = [] # <-- Lista principal.
pessoas = [] # <--Lista temporaria.
maior = menor = 0 # <-- Declarando 2 variaveis com o mesmo valor.

while True: # Loop infinito.
    pessoas.append(str(input('Nome: '))) # <-- Usuario vai adicionar o nome 
    pessoas.append(float(input('Peso: '))) # <-- e o peso.
    
    if len(dados) == 0: # <-- Lendo o comprimento da lista "dados" onde vai estar os valores do usuarios.
        maior = menor = pessoas[1] # <-- Comparando o MAIOR E O MENOR dentro da 
        #lista pessoas[1] na posicao 1 onde contem o nome dos usuarios.
    else:
        if pessoas[1] > maior: # <-- Se a pessoas[1] for maior que o maior 
            maior = pessoas[1] # então o maior passa a ser a pessoas[1].
        elif pessoas[1] < menor: # <-- Se não, se a pessoa[1] for menor que o menor
            menor = pessoas[1]  # então o menor passa a ser a pessoas[1].

    dados.append(pessoas[:]) # <-- Fazendo um COPIA da lista temporaria.
    pessoas.clear() # <-- Limpando os valores da lista temporaria.

    # <-- Valida a resposta do usuario, se ele deseja continuar.
    op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if op in 'Nn':
        break

print('=-' * 40)  
print(f'Ao todo, você cadastrou {len(dados)} pessoas.') # <-- Mosta quantas pessoas foram cadastradas.

## <-- listagem de pessoas com o MAIOR E O MENOR peso.
print(f'O maior peso foi de {maior}Kg. ', end='') # <-- Vai mostrar as pessoas mais gordas
for p in dados: 
    if p[1] == maior: # <-- Vai pegar o nome das pessoas como os maiores peso na lista.
        print(f'[{p[0]}] ', end='')
print()

print(f'O menor peso foi de {menor}Kg. ', end='') # <-- Vai mostra as pessoas mais magras 
for p in dados:
    if p[1] == menor: # <-- Vai pegar o nome das pessoas mais magras.
        print(f'[{p[0]}] ', end='')
print()


# for peso in dados:
#     print(peso[1])

#     if peso == 0:
#         maior = menor = peso[1]
#     else:
#         if peso[1] > maior:
#             maior = peso[1]
#         elif peso[1] < menor:
#             menor = peso[1]

# for p in dados:
#     if p[1] > 89:
#         print(f'Gordo: {p[0]} com {p[1]}Kg')
        
#     else:
#         print(f'Magrelo: {p[0]} com {p[1]}Kg')

# print(f'O menor peso foi de {}Kg. ')
