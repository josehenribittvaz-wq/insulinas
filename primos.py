numero = int(input("qual numero quer saber?"))
veredito = 0
for x in range (1, numero):
    resultado = numero % x
    if resultado == 0:
        veredito = veredito + 1

if veredito <= 2:
    print(f"{numero} é primo!")

else:
    print(f"{numero} não é primo!")