numescrito = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
              'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
              'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
              'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
              'Dezenove', 'Vinte')

while True:
    num = int(input('Digite uma valor entre 0 E 20: '))

    if 0 <= num <= 20:
        print(f'O número digitado foi {numescrito[num]}')
        opcao = str(input('Você deseja continuar [S]-> SIM ou [N]-> NÃO? ')).strip().upper()[0]
        if opcao == 'S':
            continue
        else:
            break

    print('Tente novamente. ', end='')

print(f'O número digitado foi {numescrito[num]}')
