c1 = 0
c2 = 0
c3 = 0
c4 = 0
nulo = 0
branco = 0

for i in range(1,21):
    voto = int(input("Digite seu candidato: "))
    if voto == 1:
        c1 += 1
    elif voto == 2:
        c2 +=1
    elif voto == 3:
        c3 += 1
    elif voto == 4:
        c4 += 1
    elif voto == 5:
        nulo += 1
    elif voto == 6:
        branco += 1

print(f"Votos para canditado 1: {c1}")
print(f"Votos para canditado 2: {c2}")
print(f"Votos para canditado 3: {c3}")
print(f"Votos para canditado 4: {c4}")
print(f"Votos nulos: {nulo}")
print(f"Votos em branco: {branco}")

total = c1+c2+c3+c4+nulo+branco
porcennulo= nulo/20 *100
porcenbranco= branco/20 *100

print(f"Porcentagem nulo: {porcennulo}")
print(f"Porcentagem branco: {porcenbranco}")
    

