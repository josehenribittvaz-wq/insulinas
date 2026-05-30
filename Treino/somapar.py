numero = int(input("Fale um numero:"))
soma = 0

for x in range(numero + 1):
    resultado = x % 2
    if resultado == 0: 
        soma += x
       
print("resultado:", soma)