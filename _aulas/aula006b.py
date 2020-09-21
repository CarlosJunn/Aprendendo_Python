n = input('digite algo: ')

print(type(n))
print('Digitou um numero: ', n.isnumeric())
print('Digitou uma letra: ', n.isalpha())
print('Digitou um caractere alpha numerico: ', n.isalnum())
print('Digitou somente letras maiusculas? ', n.isupper())