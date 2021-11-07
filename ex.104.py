# Meu programa
def leiaInt(num=input('Digite um número: ')):
    """
    -> leiaInt(num=input())
    :num: Recebe um valor numérico inteiro.
    :return: Retorna o valor recebido.
    """
    while True:
        if num.isnumeric():
            break    
        else:
            print('\033[31mERRO! Digite um número inteiro.\033[m')
            num = input('Digite um número: ')
    return num

n = leiaInt()
print(f'Você digitou o número {n}')
# ------------------------------------------------------
# Código do Guanabara
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! Digite um número inteiro.\033[m')
        if ok:
            break
    return valor

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')