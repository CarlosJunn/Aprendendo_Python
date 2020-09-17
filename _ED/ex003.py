def avaliacao(n1, n2):
    nota = (n1 * 0.40) + (n2 * 0.60)
    if nota == 0:
        return (nota,'SR')
    elif nota >= 0.1 and nota < 2.9:
        return (nota,'II')
    elif nota >= 3.0 and nota < 4.9:
        return (nota,'MI')
    elif nota >= 5.0 and nota < 6.9:
        return (nota,'MM')
    elif nota >= 7.0 and nota < 8.9:
        return (nota,'MS')
    else:
        return (nota,'SS')
    
n1 = int(input())
n2 = int(input())
print('{}'.format(avaliacao(n1, n2)))
