# O loop for (laço de repetição for)

lista_numeros = [54, 23, 18, 99, 15]

i = 0
while i < len(lista_numeros):
  print(lista_numeros[i], end= "")
  i += 1

print()
for elemento in lista_numeros:
    print(elemento, end= "") 

print()
i = 0
for el in lista_numeros:
   print(f"indice = {i}, elemento = {el}")
   i += 1

for elemento in enumerate(lista_numeros):
 print(elemento)

for indice, elemento in  enumerate(lista_numeros):
  print("indice:", indice, "elemento", elemento)

for numero in range(9):
   print(numero)

for numero in range(1, 9):
   print(numero)

print()
for numero in range(1, 9, 2):
    print(numero)

print()
lista_com_range = list(range(1, 11))
print(lista_com_range)

for letra in "Ciencia de dados":
  print(letra)

escola = "Angelo mendes"
print("O indice 7 da string escola é: ", escola[7])

lista = []
texto = "hoje é terça feira!"
for letra in texto:
  lista.append(letra)

print(lista)

for letra in lista:
  print(letra, end="")

#faça uma lista de numeros de 1 até 20 e some os pares usando range e for e mostre a some:
lista2 = list(range(1, 21))
print(lista2)
soma = 0
for numero in lista2:
  if numero % 2 == 0:
    soma += numero
print()
    