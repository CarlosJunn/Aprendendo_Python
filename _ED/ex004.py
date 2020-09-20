def pega_lista(lista):
    tamanho = int(input('Digite o tamanho da lista: '))
    contador = 0
    while contador < tamanho:
        lista.append(input())
        contador+=1
    return lista

def remove_duplicatas(lista):
     ordenada = []
     for i in lista:
         if i not in ordenada:
             ordenada.append(i)
     return ordenada

lista = []
pega_lista(lista)
print(remove_duplicatas(lista))