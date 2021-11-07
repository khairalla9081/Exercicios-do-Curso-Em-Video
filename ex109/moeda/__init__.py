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