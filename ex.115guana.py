from ex115gb.lib import arquivo
from ex115gb.lib.interface import *
from ex115gb.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt' # Nome do aquivo.

if not arquivoExiste(arq): # Verifica a criação do arquivo.
    criarArquivo(arq) # Caso não exista a função criarArquivo é passada.

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)

    elif resposta == 2:
        # Opção de cadastrar uma nova pessoas.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        # Opção de sair do sistema.
        cabeçalho('Saindo do sistema... Até logo!')
        break

    else:
        # Digitou uma opção errada do menu.
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
