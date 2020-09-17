def analisa(n1,n2):
    if n1 > n2:
        print('{}\n{}'.format(n1,n2))
    if n1 < n2:
        print('{}\n{}'.format(n2,n1))
    if n1 == n2:
        print('{}\n{}'.format(n1,n2))
        print('iguais')
    else:
        print('diferentes')

n1 = int(input())
n2 = int(input())
analisa(n1,n2)
