def fatorial(num, show=False):
    """
    -> Calculo o fatorial de um número.
    :para n: O número a ser calculado.
    :para show: (opcional) Mostra ou não a conta.
    :return: 0 valor do fatorial de um número n.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show == True:
            print(f'{c}', end='')
            print(f' X ' if c > 1 else ' = ', end='')
        
    return print(f)
        

n = int(input('Número para calcular o seu fatorial: '))
fatorial(n, show=True)