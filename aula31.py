# DICIONARIO X CONJUNTO X LISTA X TUPLA

n1 = 9
n2 = 7
n3 = 13

numeros = [9, 7, 13] # é uma lista
numeros.append(21)
numeros.remove(9)
print(numeros[0])

numeros = (9, 7, 13) # é uma tupla
# não tem como adicionar, remover
print(numeros[0])

conjunto = set()
conjunto.add(9)
conjunto.add(7)
print(conjunto)
# print(conjnto[0]) conjunto não tem ordem, então não tem indice

conjunto = {"Ana", "Carol", "Maria", "Paula"}
print(conjunto)
print(conjunto)
print(conjunto)

print()
for item in conjunto:
    print(item)

# DICIONARIO

dicionario = {}
dicionario = dict()

dicioanrio = {"Chave":"Valor", "Chave1":"Valor1"}

estados = {"SP":"São Paulo", "RJ":"Rio", "MG":"Minas"}
print()
print(estados)
for item in estados:
    print(item)

    print()
    for item in estados:
        print(estados[item])

print()
for chaves in estados.keys():
    print(chaves)

    print()
for valor in estados.values():
    print(valor)

print()
for chave, valor in estados.items():
    print(chave, valor)

print()
estados["RJ"] = "Rio de Janeiro"
print(estados["RJ"])

estados["ES"] = "Espirito Santo"
print()
print(estados)

del estados["SP"]
print()
print(estados)

print()
for enumerado, (i, v) in enumerate(estados.items(), start=1):
    print(enumerado, i, v)