import random
caracter = "ABCDEFGHIJKLMNOPQRVXZTW/&%$#"
longitud = int(input("introduce una longitud de contraseña:"))
password = ""
for i in range(longitud):
    x =random.choice(caracter)
    password += x   
print(password)
