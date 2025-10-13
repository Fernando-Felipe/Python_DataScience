letra = input("Digite a Letra: ")
v = "aeiou"

if(letra in v):
    print(f"{letra} e uma vogal")
else:
    print(f"{letra} e uma consoante")