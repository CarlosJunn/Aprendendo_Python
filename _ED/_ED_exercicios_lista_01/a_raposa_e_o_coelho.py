def escapa_coelho(coelho, raposa, nb):
    escapatoria = 0
    xr, yr = (float(num) for num in raposa.split())
    xc, yc = (float(num) for num in coelho.split())
    for i in range (nb):
        xb, yb = (float(num) for num in input().split())
        BC = ((xc - xb)**2 + (yc - yb)**2) ** 0.5
        BR = ((xr - xb)**2 + (yr - yb)**2) ** 0.5
        if BC <=  (BR / 2):
            escapatoria += 1
            print('O coelho pode escapar pelo buraco ({:.3f}, {:.3f}).'.format(xb, yb))
            break
    return escapatoria

nb = int(input())
coelho = input()
raposa = input()

if escapa_coelho(coelho, raposa, nb) == 0:
    print('O coelho nao pode escapar.')