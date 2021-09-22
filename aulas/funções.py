# def lin():
#     print('-' * 30)


# lin()
# print('guga')
# lin()

# def mensagem(msg):
#     print('-=' * 30)
#     print(msg)
#     print('-=' * 30)


# mensagem('MAMACO do Cão')
#-------------------------------------

# def soma(a, b):
#     s = a + b
#     print(s)


# soma(a=3, b=5)

# def soma(a, b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma A + B = {s}')
    

# soma(5, 3)]

# def contador(*num):
#     for v in num:
#         print(f'{v} ', end='')
#     print('fim')

# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)

# def contador(*num):
#     tam = len(num)
#     print(f'tamanho é {tam}')


# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)

# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos += 1

# valores = [6, 2, 3, 1, 3, 4]
# dobra(valores)
# print(valores)


def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os {valores} temos {s} ')


soma(5, 2)
soma(2, 9, 4)