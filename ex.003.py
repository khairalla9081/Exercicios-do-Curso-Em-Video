n1 = int(input('Digite um número: '))      # O usuario vai digiatar um número!
n2 = int(input('Digite outro número: '))   # O usuario vai digitar outro número!
s = n1 + n2                                # Aqui o programa vai calcular os 2 valores!
print('A soma entre \033[34m{}\033[m e \033[31m{}\033[m vale \033[4;43m{}\033[m'.format(n1, n2, s))
# Aqui o programa vai mostra a soma entre os 2 números,
# e o primeiro valor vai ficar azul, o segundo da cor vermelha,
# e o resultado cai ficar sublinahdo com o fundo amarelo.
