#aula21.py

# EXERCICIOS DE FIXAÇÃO

# 1.adicione o numero 50 ao final da lista.
lista_numeros= [10, 20, 30, 40]
lista_numeros.append(50)
print(lista_numeros)

# 2.adicione "laranja" ao indice 1 da lista.
lista_frutas = ["maçã", "banana", "uva"]
lista_frutas.insert(1, "laranja")
print(lista_frutas)


# 3.remova "cachorro" da lista.
lista_animais = ["cachorro", "gato", "passaro", "cachorro"]
while "cachorro" in lista_animais:
 lista_animais.remove("cachorro")
print(lista_animais)

# 4. Remova o elemento de indice 2 da lista mostre o elemento removido.
lista_nomes = ["alice", "bob", "charlie", "David"]
valor_removido = lista_nomes.pop(2)
print(lista_nomes)
print(valor_removido)


# 5. encontre o indice da primeira ocorrencia de "azul" na lista.
lista_cores = ["vermelho", "azul", "verde", "amarelo", "azul"]
índice_azul = lista_cores.index('azul')
print(índice_azul)

# 6. conte quantas vezes o numero 2 aparece na lista.
lista_numeros_repetidos = [1, 2, 3, 2, 4 , 2, 5, 2]
quantidade_de_dois = lista_numeros_repetidos.count(2)
print(quantidade_de_dois)


# 7. ordene a lista em ordem crescente.
lista_desordenada = [50, 20, 80, 10, 40]
lista_desordenada.sort()
print(lista_desordenada)

