d = int(input('Quantos dias alugados: '))
km = float(input('Quantos Km percorreu no carro alugado: Km'))

aluguel = (d * 60) + (km * 0.15)

print('O aluguel do carro custou: R${:.2f}'.format(aluguel))