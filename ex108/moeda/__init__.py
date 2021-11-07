def metade(n):
    return n / 2


def dobro(n):
    return n * 2


def aumentar(n, v):
    return n + (n * v) / 100


def diminuir(n, v):
    return n - (n * v) / 100


def moeda(valor):
    inteiro = int(valor)
    forma = f'R${inteiro},00'
    return forma

# def moeda(preço=0, moeda='R$'):
#     return f'{moeda}{preço}'.replace('.',',')