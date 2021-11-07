from random import randint

number = []

def sorteia():
    for i in range(5):
        number.append(randint(0, 50))
    print(f'Os valores sorteados foram {number}')


def somaPar():
    par = []
    for n in number:
        if n % 2 == 0:
            par.append(n)
    soma = 0
    for s in par:
        soma += s
    print(f'O valores pares foram {par} e sua soma é {soma}')

    

sorteia()
somaPar()