n = int(input("Digite o numero: "))
c = 0
for i in range(1,n):
    if n% i == 0:
        c += 1

if c == 1:
    print(f"{n} e primo")
else:
    print(f"{n} nao e primo")
