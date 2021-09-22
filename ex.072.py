numescrito = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
              'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
              'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
              'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
              'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número de 0 A 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'O número digitado foi {numescrito[num]}')
