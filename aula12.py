# 1. faça um programa que peça  a idade do usuário e imprima se ele é maior ou menor de 18 anos

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("é de maior!")
else:
    print("é de menor")

# 2. faça um programa que peça um número e mostre se ele é positivo ou negativo.

numero = int(input("Digite um número inteiro: "))

if numero >= 0:
    print("o numero é positivo!")
else:
    print(" o numero é negativo!")

# 3. faça um programa que, dado um numero digitado, mostre se ele é par ou impar

numero = int(input("Digite um numero inteiro: "))
if numero % 2 == 0:
    print("o numero é par.")
else:
    print("o numero é impar. ")


# 4 faça um programa que peça dois números e mostre o maior deles.

n1 = int(input("Digite um inteiro"))
n2 = int(input("Digite outro inteiro"))

if n1 > n2:
    print(n1)
else:
    print(n2)
# 5. faça um programa que leia a validade das informações:
# a. idade: entre 0 e 150;
# b. salário: maior que 0;
# c. sexo: m, f ou outro;

idade = int(input("Digite a idade maior que 0 menor 150. "))
if idade > 0 and idade < 150:
    print("idade válida")
else:
    print("idade inválida")

    salario = int(input("Digite o salario: R$ "))
    if salario > 0:
        print(f" O salario é R$ (salario)")
    else:
        print("salario inválido")

        sexo = input("Digite o sexo [M, F, outro]: ")
    if sexo.upper == "M":
        print("sexo masculino")
    elif sexo.upper == "F":
        print("sexo feminino.")
    elif sexo.lower == "outro":
        print("sexo outro")
    else:
        print("sexo inválido")
