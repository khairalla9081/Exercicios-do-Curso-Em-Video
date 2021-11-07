from ex115gb.lib.interface import *


def arquivoExiste(nome):
    """
    >> A função arquivoExiste(nome) verifica a existencia de um arquivo,
    caso esse arquivo já exista ele vai retornar True, mas caso exista um exception
    'FileNotFoundError' ele vai retornar False.
    :name: Parametro do nome do arquivo.
    :return: False or True.
    """
    try:
        a = open(nome, 'rt') # 'rt' leitura em modo texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    """
    >> A função criarArquivo(nome) faz a ciração de um arquivo
    :nome: Parametro para o nome do arquivo.
    :return: None.
    """
    try:
        a = open(nome, 'wt+') # 'wt+' escreve em modo texto e o '+' cira o arquivo caso não exista. 
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    """
    >> A função lerArquivo(nome) faz a leitura do conteudo do arquivo.
    :nome: Parametro do nome do arquivo
    :return: None
    """
    try: # Faz a tentativa para abrir o arquivo.
        a = open(nome, 'rt') # abre e faz a leitura em modo texto.
    except: # Caso de erro ao ler o arquivo.
        print('Erro ao ler o arquivo!')
    else: # Faz a leitura do arquivo.
        cabeçalho('PESSOAS CADASTRADAS')
        #print(a.read())    # read() -> Le todo o conteudo  # readlines() -> Le cada linha
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally: # Fecha o arquivo.
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    """
    >> A função 'cadastrar' faz o cadastro de um novo usuário no arquivo.
    :arq: Nome do arquivo.
    :nome: Recebe o nome do novo usuário, caso não passado o nome por padrão será 'desconhecido'.
    :idade: Recebe a idade do novo usuário. 
    """
    try:
        a = open(arq, 'at') # 'at' adiciona um conteudo no arquivo em modo texto.
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n') # escreve o nome e a idade do novo usuário.
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()


