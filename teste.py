s1 = 'oi'
s2 = "ola"
texto = " isabelle vivam "

#print(type(s1),type(s2))
print("texto antes dos metodos")
print(texto)
print("texto depois dos metodos")
texto = texto.strip().replace("m", "n").upper()
print(texto)

