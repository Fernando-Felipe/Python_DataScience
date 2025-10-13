coloniaA = 4
coloniaB = 10
i = 0
while coloniaA < coloniaB:
     coloniaA = coloniaA * 0.03 + coloniaA
     coloniaB = coloniaB * 0.015 + coloniaB
     i += 1


print(f"foram {i} dias")