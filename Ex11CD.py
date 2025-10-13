lado1 = int(input("Digite lado: "))
lado2 = int(input("Digite lado: "))
lado3 = int(input("Digite lado: "))

if lado1 + lado2 > lado3 or lado2 + lado3 > lado1 or lado1 + lado3 > lado2:
    print("pode se formar um triangulo")
    
    if lado1 == lado2 == lado3:
        print("Equilatero")
    elif lado1 == lado2 != lado3 or lado2 == lado3 != lado1 or lado1 == lado3 != lado3:
        print("Isoceles")
    elif lado1 != lado2 != lado3:
        print("Escaleno")