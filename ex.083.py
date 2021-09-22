expr = str(input('Digite uma empressao: '))
pilha = []

for s in expr:
    if s == '(':
        pilha.append('(')
    elif s == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressao esta valida!')
else:
    print('Sua expressao esta errada!')
