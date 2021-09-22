house = float(input('How much does house cost? R$ '))
salary = float(input('How much is your salary? R$ '))
year = int(input('How many years? '))
installment = house / (year * 12)
minimum = salary * 30 / 100
print('To buy a house of R${:.2f} in {} years'.format(house, year), end=' ')
print('you`ll pay R${:.2f} for month'.format(installment))
if installment <= minimum:
    print('\033[32mThe loan CAN be made!\033[m')
else:
    print('\033[31mThe loan CANNOT be made!\033[m')
