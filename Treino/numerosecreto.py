secreto = 10 


while True: 
    numero = int(input("Fale um número:"))
    if numero > secreto:
        print("chute alto")
    elif numero < secreto:
        print("chute baixo")
    elif numero == secreto:
            print("voce acertou")
            break