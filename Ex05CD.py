p1 = float(input("Digite produto 01: "))
p2 = float(input("Digite produto 02: "))
p3 = float(input("Digite produto 03: "))

menor = p1
if p2 < menor:
    menor = p2
if p3 < menor:
    p3 = menor


print(f"O produto mais barato e {menor}")