#pede uma palavra para o usuário
palavra = str(input("fale uma palavra:"))

vogais = "aeiou"

consoantes = "bcdfghjklmnpqrstvwxyz"

contador = 0

contador2 = 0

for x in palavra:
    for a in vogais:
        if x == a:
            contador += 1
    for b in consoantes:
        if x == b:
            contador2 += 1



print("vogais:", contador, "consoantes:", contador2)