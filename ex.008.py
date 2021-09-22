medida = float(input('Qual é a distacia de: '))
km = medida * 10000
hm = medida * 1e+6
cm = medida * 100
mm = medida * 1000
print('A medida de {} coresponde a  \n{}km \n{:.2f}hm \n{:.0f}cm \n{:.0f}mm'.format(medida, km, hm, cm, mm))
