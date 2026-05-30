senha = 1234

while True: 
    numero = int(input("fale a senha:"))
    if numero == senha:
      print("senha correta")
      break
    else: 
       print("senha incorreta!!")
