from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(num)
print(f'O maior numero sorteado foi: {max(num)}')
print(f'O menor numero sorteado foi: {min(num)}')
