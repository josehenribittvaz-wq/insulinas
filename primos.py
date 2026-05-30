#PEDINDO UM NÚMERO AO CLIENTE
numero = int(input("qual numero quer saber?"))

#VARIÁVEL DO VEREDITO 
veredito = 0

#LOOP PARA CHEGAR AO RESULTADO 
for x in range (1, numero + 1):
    resultado = numero % x
    print("tentativa", x)
    #VERIFICAÇÃO PARA VER SE O RESULTADO É IGUAL A ZERO, SE FOR ADICIONA MAIS 1 AO VEREDITO
    if resultado == 0:
        veredito = veredito + 1

if veredito == 2:
    print(f"{numero} é primo!")


else:
    print(f"{numero} não é primo!")