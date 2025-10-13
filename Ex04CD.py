ano1 = float(input("Digite valo no ano 01: "))
ano2 = float(input("Digite valo no ano 02: "))
ano3 = float(input("Digite valo no ano 03: "))

if ano1 > ano2 and ano1 > ano3:
    print("Ano 1 Maior")
elif ano2 > ano1 and ano2 > ano3:
    print("Ano 2 Maior")
else:
    print("Ano 3 Maior")

if ano1 < ano2 and ano1 < ano3:
    print("Ano 1 Menor")
elif ano2 < ano1 and ano2 < ano3:
    print("Ano 2 Menor")
else:
    print("Ano 3 Menor")