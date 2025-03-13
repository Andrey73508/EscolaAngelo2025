valor = int(input("Digite um inteiro entre 10 e 100"))

if valor <= 10 or valor >= 100:
    print("valor inválido")
else:
    if valor % 2 == 0:
        if valor == 50:
          print("voce digitou 50")
        else:
            print("voce não digitou 50")
    else:
        print("o valor é impar")

