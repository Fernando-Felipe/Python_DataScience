n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

print("Par / Inteiro / Positivo")
op = input("digite a oprecao: ")

if op == "Par":
    if n1%2 == 0:
        print(f"{n1} e par ")
    else:
        print(f"{n1} e impar")
    if n2%2 == 0:
        print(f"{n2} e par ")
    else:
        print(f"{n2} e impar")

elif op == "Inteiro":
    if n1%1 == 0:
        print(f"{n1} e inteiro")
    else:
        print(f"{n1} decimal")
    if n2%1 == 0:
        print(f"{n2} e inteiro")
    else:
        print(f"{n2} decimal")

elif op == "Positivo":
    if n1 > 0:
        print(f"{n1} e positivo")
    else:
        print(f"{n1} e negativo")
    if n2 > 0:
        print(f"{n2} e positivo")
    else:
        print(f"{n2} e negativo")

