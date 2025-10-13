print("Maior numero")
n1 = int(input("Digite o primeiro numero: ")) 
n2 = int(input("Digite o segundo numero: "))

if(n1>n2):
    print(f"{n1} maior que {n2}")
elif(n2>n1):
    print(f"{n2} maior que {n1}")
else:
   print(f"{n1} e {n2} sao iguais")