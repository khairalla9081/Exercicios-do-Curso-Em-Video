## Meu codigo.
#================================================================

listNum = []

for i in range(1, 6):
    listNum.append(int(input(f'Digite o valor {i}: ')))
    
    for num in range(len(listNum) -1, 0, -1):
        for i in range(num):
            if listNum[i] > listNum[i + 1]:
                temp = listNum[i]
                listNum[i] = listNum[i + 1]
                listNum[1 + i] = temp
            i += 1

print('*' * 60)
print(f'A lista ordenada: {listNum}')

## Codigo do Guanabara.
#================================================================

lista = list()

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
            lista.append(n)
            print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adiconado na posicao {pos} da lista...')
                break
            pos += 1

print('==' * 40)
print(f'Os valores digitados em ordem foram: {lista}')

## Codigo do comentario do youtube.
#================================================================

numeros = []
for c in range(5):
    num = int(input('Digite um valor: '))

    for i, v in enumerate(numeros):
        if num < v:
            numeros.insert(i, num)
            print(f'Adicionado na posição {i} da lista...')
            break

    if len(numeros) < c + 1:
        numeros.append(num)
        print('Adicionado ao final da lista...')

print('-=' * 28)
print(f'Os valores digitados em ordem foram: {numeros} ')
