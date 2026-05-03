#crear un mini sitema bancario de registro de un cliente
#SU BANCO NICK ;)

#parte1:
cliente1 = {
    'nombre' : 'Lucas Peréz',
    'edad' : 25,
    'saldo' : 10000.0,
    'tarjeta_de_credito' : True,
    'PIN' : '1234',
    'ciudad' : 'Madrid',
    'cedula' : 11111111,
    'apertura_cuenta' : '12_02_2025'
}

pin_usuario = '1234'

sedes_banco = { 'Bogotá','Barranquilla','Madrid','Madrid'}

#parte2:
movimientos = [200000, -50000, 150000, -30000]
datos_inamovibles = ( cliente1['ciudad'], cliente1['cedula'], cliente1['apertura_cuenta'])

#datos_inamovibles['PIN'] = 425426 #(error)


#print(sedes_banco['Bancolombia'], sedes_banco['Banco Popular']) observacion del conjunto con los duplicados

#parte3
saldo_total = movimientos[0]+ movimientos[1] + movimientos[2] + movimientos[3] + cliente1['saldo']

print(f'Bienvenido {cliente1["nombre"]}, tu saldo actual es: ${saldo_total}, tipo de dato: {type(saldo_total)}')
gasto_mensual = 80000

meses_duracion = saldo_total // gasto_mensual


print(f'Con tu saldo actual gastando ${gasto_mensual} al mes, sobrevivirias {meses_duracion} meses')

#Parte4  — Operadores de comparación y lógicos
print('El cliente es mayor de edad?: ', cliente1['edad'] > 18)
print('¿Su saldo nuevo es mayor o igual a $500.000: ', cliente1['saldo'] >= 500000 )
print('¿Su ciudad está en el conjunto de ciudades del banco?', cliente1['ciudad'] in sedes_banco, ':' ,cliente1['ciudad'])
print('¿El cliente es mayor de edad y tiene saldo positivo?', (cliente1['edad'] >= 18) & (cliente1['saldo'] > 0))
print('¿El cliente no tiene tarjeta de crédito o su saldo es mayor a $1.000.000?', (cliente1['tarjeta_de_credito'] == True) | (cliente1['saldo'] > 1000000))

#parte5 - Condicionales
print('Los pines coinciden? : ')
if (pin_usuario == cliente1['PIN']):
    print ('acceso concedido')
else:
    print ('acceso denegado')    

if saldo_total > 5000000:
    print("Cliente premium")
elif saldo_total > 1000000:
    print("Cliente estandar")
elif saldo_total > 0:
    print("saldo bajo, considere depositar")
else:
    print("Cuenta en numeros rojos")

#Aprobacion de credito
if cliente1['edad'] >= 18:
    if (saldo_total > 500000) & (cliente1['tarjeta_de_credito']==False):
        print("Puede solicitar tarjeta de credito")
    elif cliente1['tarjeta_de_credito'] == True:
        print("Ya tiene tarjeta activa")
    else:
        print("saldo insuficiente para tarjeta")         
else:
    print("No cumple el requisito de edad para una tarjeta de credito")
