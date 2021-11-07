from ex115 import *
from time import sleep

cor = (
'\033[m',    # branco
'\033[31m',  # vermelho
'\003[34m',  # azul
'\033[33m',  # amarelo
'\033[32m'   # verde
)

menu()

## Programa principal 
while True:
    try:
       op = int(input('\033[32mSua Opção:\033[m '))
    except (ValueError, TypeError):
        print('\033[31mERRO: digite uma opção valida.\033[m')
        sleep(1)
        menu()
        continue

    if op == 1:
        print(listapessoas)
    
    elif op == 2:
        nome = str(input('Digite o nome: '))
        idade = int(input('Digite a idade: '))
        print(put(nome, idade))

    elif op == 3:
        sleep(1)
        line()
        print('\033[35mSaindo do sistema...\033[m'.center(40))
        line()
        break
    
    else:
        print('\033[31mERRO: digite uma opção valida.\033[m')
        sleep(1)
        menu()
        continue
