import math
a = float(input('Digite um angulo: '))
seno = math.sin(math.radians(a))
print('O angulo de {} tem o SENO de {:.2f}'.format(a, seno))
cos = math.cos(math.radians(a))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(a, cos))
tan = math.tan(math.radians(a))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(a, tan))