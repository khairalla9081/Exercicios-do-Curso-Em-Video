from time import sleep


def contador():
    print('Contade de 1 até 10 de 1 em 1')
    for i in range(1, 11):        
        print(i, end=' ' )
    print('FIM')

    print('Contade de 10 até 0 de 2 em 2')
    for i in range(10, -1, -2):
        print(i, end=' ')
    print('FIM')

    print('Agora é sua vez de personalizar a contagem!')





contador()



    # for i in range(inicio, fim+1, passo):
    #     print(i, end=' ')
    # print('FIM')

    # for i in range(inicio, fim, passo+2):
    #     print(i, end=' ')
    # print('FIM')