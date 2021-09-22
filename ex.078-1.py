# ESSE FOI MEU CODIGO FEITO SEM TRATAMENTO PARA NUMEROS DIGITADOS IGUAL.
num = list()

for c in range(0, 5):
    num.append(int(input(f'Digite um valor na posição {c}: ')))

print(num)
print(f'O maior numero foi {max(num)} na posição {num.index(max(num))}')
print(f'E o menor numero foi {min(num)} na posição {num.index(min(num))}')
print('fim')

# ESSES FOI A RESOLUÇÃO DO Curso em Video.
lista_num = []  # FOI CRIADO UMA LISTA VAZIA
maior = menor = 0   # OS VALORES MAIOR E MENOR ESTÃO COMEÇANDO COM O VALOR "0"

for c in range(0, 5):   # AQUI FOI CRIADO UM LAÇO DE REPETIÇÃO COM O "FOR" PARA GERAR 5x O "append" PARA DIGITAR OS SEGUINTES VALORES
    lista_num.append(int(input(f'Digite um valor na posição {c}: ')))  # SERÁ DIGITADO OS VALORES DENTRO DA LISTA
    if c == 0:
        maior = menor = lista_num[c]
# AQUI ESTÁ SENDO COMPARADO SE O PRIMEIR0 VALOR É MAIR OU MENOR
# POREM COMO É O PRIMEIRO VALOR ELE VAI SER O MAIOR É O MENOR.
    else:
        if lista_num[c] > maior:  # SE O NUMERO FOR MAIOR QUE O NUMERO ANTERIOR
            maior = lista_num[c]  # O VALOR DE LISTA_NUM PASSA A SER O MAIOR
        elif lista_num[c] < menor:  # SE O NUMERO FOR MENOR QUE O NUMERO ANTERIOR
            menor = lista_num[c]  # O VELOR DE LISTA_NUM PASSA SER O MENOR
print('=-=' * 30)
print(f'Você digitou os valores {lista_num}')
print(f'O maior numero digitado foi {maior} nas posições ', end='')
for i, v in enumerate(lista_num):  # AQUI O "FOR" VAI FAZER UMA ENUMERAÇÃO COM O "ENUMERETE"
    if v == maior:  # PARA SABER A POSIÇÃO DO MAIOR
        print(f'{i}...', end='')
print()
print(f'O menor numero digitado foi {menor} nas posições ', end='')
for i, v in enumerate(lista_num):  # AQUI O "FOR" VAI FAZER UMA ENUMERAÇÃO COM O "ENUMERETE"
    if v == menor: # PARA SABER A POSIÇÃO DO MENOR
        print(f'{i}...', end='')
print()
