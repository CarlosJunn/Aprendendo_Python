# -*- coding: utf-8 -*-
arquivo = open('arquivo.txt')

#abrindo arquivo e salvando em uma lista, imprimindo linha por linha
linhas = arquivo.readlines()

for linha in linhas:
    print(linha)

#coloca tudo em uma unica variavel
texto_completo = arquivo.read()

print(texto_completo)

#criando arquivo
w = open('arquivo2.txt','w')
#escrevendo conteudo no novo arquivo
w.write('Esse é o meu arquivo\n')
#fecahndo um arquivo
w.close()