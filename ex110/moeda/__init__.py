def metade(n, format=True):
    if format == True:
        return moeda(n / 2)
    else:
        return n / 2

def dobro(n, format=True):
    if format == True:
        return moeda(n * 2)
    else:
        return n * 2


def aumentar(n, v, format=True):
    if format == True:
        return moeda(n + (n * v) / 100)
    else:
        return n + (n * v) / 100


def diminuir(n, v, format=True):
    if format == True:
        return moeda(n - (n * v) / 100)
    else:
        return n - (n * v) / 100


def moeda(valor):
    inteiro = int(valor)
    forma = f'R${inteiro},00'
    return forma


def resumo(valor, aumento=10, baixo=5):
    print('--' * 15)
    print('RESUMO DO VALOR'.center(15))
    print('--' * 15)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor)}')
    print(f'Metade do preço: \t{metade(valor)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento)}')
    print(f'{baixo}% de redução: \t{diminuir(valor, baixo)}')
    print('--' * 15)
