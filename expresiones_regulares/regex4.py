import re

email = "example@gmail.com"

pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]+\.[a-zA-Z]{2,}"

result = re.match(pattern, email)

if result:
    print("Direccion de correo válida")
else:
    print("Direccion de correo invalida")
