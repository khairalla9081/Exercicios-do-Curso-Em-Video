def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except (ValueError, TypeError):
            print('\033[31mDigite um Valor inteiro!\033[m')
            continue
        except KeyboardInterrupt:
            print('\nO usuário decidou interromper o programa.')
            break


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc
