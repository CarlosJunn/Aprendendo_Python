# -*- coding: utf-8 -*-
a = "Diego"
b = "Mariano"

concatenar = a + " " + b + "\n"

print(concatenar)
print(concatenar.lower()) #lower transforma tudo em minúsculo
print(concatenar.upper()) #upper transforma tudo em maiúsculo
print(concatenar.strip()) #strip remove todos os espaços e caracteres especiais da str

#split converte a senquencia em uma lista
minha_string = "O rato roeu a roupa do rei de Roma"

minha_lista = minha_string.split() #recebe como parametro o caractere separador entre (" ")
print(minha_lista)

