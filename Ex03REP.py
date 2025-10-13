for i in range(1,4):
    nota = int(input("Digite o a nota: "))
    while nota>5 or nota<0:
        nota = int(input("Digite o a nota novamente: "))


print("notas validas")