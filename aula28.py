# OUTRAS ESTRUTURAS DE DADOS: Tuplas, conjuntos e dicionários

r = range(1, 9)
print(r)

for item in r:
    print(item)

lista = list(r)
print(list)

lista_vazia = []
lista_vazia = list()

tupla = ()
tupla = tuple()

tupla = tupla(r)
print(tupla)

lista = ["Ana", "Paula", "Sofia"]
tupla = ("Ana", "Paula", "Sofia")

print(lista)
print(tupla) 

lista.append("Isabelly")
tupla # NÃO TEM COMO ADICIONAR, RETIRAR OU MODIFICAR APOS CRIAÇÃO

conjunto = {}
conjunto = set()

conjunto = set(r)
print(conjunto)

conjunto.add("19")
print(conjunto)

dicionario = {}
dicionario = dict()

dicionario = {"SP": "São Paulo", "RJ": "Rio", "ES": "Espirito Santo", "MG": "Minas Gerais"}
print(dicionario)
print(dicionario["SP"])

dicionario_nomes = {0:"Ana", 1:"Maria", 2:"Carol", 3:"Cristal", 4:"Isabelly"}

print(dicionario_nomes[1])

dicionario_países = {55:"BR", 1:"USA", 23:"UK",}

print(dicionario_países[55])
# print(dicionario_países[10])