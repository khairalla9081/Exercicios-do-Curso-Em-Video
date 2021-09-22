def linha(): # Função para printar uma linha
    print('-=' * 10)


def area(l, c): # Função para o calculo da área
    calculo = l * c
    print(f'A área de um terreno {l:.2f} X {c:.2f} é de {calculo:.2f}m².')


print('Controle de terrenos')
linha()
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento) # Recebe os paramentros das variaveis acima.
