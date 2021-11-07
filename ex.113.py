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


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
            return num
        except (ValueError, TypeError):
            print('\033[31mDigite um Valor real!\033[m')
            continue
        except KeyboardInterrupt:
            print('\nO usuário decidou interromper o programa.')
            break


n1 = leiaInt('Digite um número inteior: ')
n2 = leiaFloat('Digite um número real: ')
print(f'O número inteiro foi {n1} e o valor real foi {n2}')