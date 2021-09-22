older = men = women = 0
while True:
    age = int(input('How old are you? '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('What is your genre? [M/F] Male or Female: ')).strip().upper()[0]
    if age >= 18:
        older += 1
    if sex == 'M':
        men += 1
    if sex == 'F' and age < 18:
        women += 1
    option = ' '
    while option not in 'YN':
        option = str(input('Would you like to continue? [Y/N] Yes or Not: ')).strip().upper()[0]
    if option == 'N':
        break
print(f'We have {older} older people.')
print(f'We have {men} men registered.')
print(f'And we have {women} women registered.')
