n = int(input('Digite um numero para ver sua tabuada: '))
print('='*12)
for i in range (10):
    print('{:2} x {} = {}'.format(i + 1, n, (i + 1)*n))
print('='*12)