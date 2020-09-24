larg = float(input('largura da parede: '))
alt = float(input('altura da parede: '))
área = larg * alt
print('Sua parede tem uma dimensão de {:.2f}x{:.2f} e sua área é de {:.2}m²'.format(larg, alt, área))
tinta = área / 2
print('para pintar essa parede usará {:.2f} L de tinta'.format(tinta))