## Vai dar erro se a divisão for = 0
# a = int(input('Numerador: '))
# b = int(input('Denominador: '))
# r = a / b
# print(f'O resultado é {r}')

# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
    
# except Exception as error:
#     print(f'Problema encontrado foi {error.__class__} ')

# else:
#     print(f'O resultado é {r:.1f}')

# finally:
#     print('Volte sempre! Muito obrigado.')

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError):
    print('Tivemos um problema com o tipos de dados que você digitou.')

except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')

except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')

except Exception as error:
    print(f'Problema encontrado foi {error.__cause__} ')

else:
    print(f'O resultado é {r:.1f}')

finally:
    print('Volte sempre! Muito obrigado.')