larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem a Dimenção de {}m X {}m e a area é de {}m²'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {:.1f}L de tinta'.format(tinta))