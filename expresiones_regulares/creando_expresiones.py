import re

#detectando un numero CABA y ocultandolo
texto = "Hola cuco, mi nuero es: +57 601 8285-502 +57 601 8285-502"

#identificando numeros colombianos
pattern = r'\+57\s\d{3}\s\d{4}-\d{3}'

reemplazo = re.sub(pattern,"(Numero oculto)",texto)

print(reemplazo)