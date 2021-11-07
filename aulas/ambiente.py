# def contador(i, f, p):
#     """
#     -> Faz uma contagem e mostra na tela.
#     :para i: Início do contagem
#     :para f: Fim da contagem
#     :para p: Passo da contagem
#     :return: sem retorno 
#     """	
#     c = i
#     while c <= f:
# 	    print(f'{c}', end='..')
# 	    c += p
#     print('FIM!')

# contador(2,10,2)
# help(contador)
#--------------------------------------------
# Se nem um valor for atribuido a c o c passa a valer 0
# def somar(a, b, c=0): # Nada me empede de fazer isso em python. 
# Tornando o código seguro, para não quebrar.
# def somar(a, b, c=0):
#     """
#     -> Faz uma contagem e mostra na tela.
#     :para a: Primeiro valor
#     :para b: Segundo valro
#     :para c: Terciro valor
#     :return: sem retorno 
#     """
#     s = a + b + c
#     print(f'A soma vale {s}')
    
# somar(3,2,5)

# def somar(a=0, b=0, c=0):
# 	s = a + b + c
# 	return s	

# # resp = somar(3, 2, 5) ou print(somar(3,2,5)
# r1 = somar(3,3,3)
# r2 = somar(2,1)
# r3 = somar(9,1)
# print(f'Meus cáculos deram {r1}, {r2}, {r3}')

# ---------------------------------------------------------

# PARTE PRATICA

# def fatorial(num=1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f

# n = int(input('Digite um número: '))
# print(fatorial(n))

# def fatorial(num=1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f

# f1 = fatorial(2)
# f2 = fatorial(8)
# f3 = fatorial()
# print(f'Os resultados são {f1}, {f2}, {f3}')

# def par(n=0):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# num = int(input('Digite um numero: '))
# print(par(num))