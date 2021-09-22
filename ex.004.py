algo = input('Digite algo: ')
# O ususario vai digitar alguma coisa.
print(type(algo))
# Vai dizer quel é o tipo da classe!
print('\033[31m {} \033[m é um numero? \033[1;33m {} \033[m '.format(algo, algo.isnumeric()))
# O programa vai dizer se é um Número!
print('\033[31m {} \033[m é uma palavra? \033[1;32m {} \033[m'.format(algo, algo.isalpha()))
# O programa vai dizer se é uma Palavra!
print('\033[31m {} \033[m é alfanumerico? \033[1;35m {} \033[m'.format(algo, algo.isalnum()))
# O programa vai dizer se é tantom um Número como uma Palavra!
print('\033[31m {} \033[m está em maiusculo? \033[1;36m {} \033[m'.format(algo, algo.isupper()))
# O programa vai dizer se Todas letras estão em MAISCULAS!
print('\033[31m {} \033[m a 1 letra está em maiusculo? \033[1;31m {} \033[m'.format(algo, algo.istitle()))
# O programa vai dizer se a Primeira letra da palavra está maiuscula
print('\033[31m {} \033[m está em minusculo? \033[1;37m {} \033[m'.format(algo, algo.islower()))
# O programa vai dizer se Todas as letras estão em minusculas!
print('\033[31m {} \033[m isso é um digito? \033[1;30m {} \033[m'.format(algo, algo.isdigit()))
# O programa vai dizer se é um Digito!
