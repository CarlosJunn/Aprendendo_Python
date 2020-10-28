# -*- coding: utf-8 -*-
minha_string = "O rato roeu a roupa do rei de Roma"

busca = minha_string.find("rei") #recebe como parametro a busca

print(busca) #mostra a posição da busca
print(minha_string[busca:]) #mostra tudo que vem após a busca

busca = minha_string.find("Rainha")
print(busca) #caso não encontre o resultado da busca retorna -1