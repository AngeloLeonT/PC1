# Establecer la edad del cliente
# Establecer el precio de la entrada
# Obtener el resultado dependiendo la edad del cliente

edad = int(input('Ingrese la edad del cliente: '))

if edad < 4 and edad >=0:
    print(f'El usuario no paga entrada')
elif edad >= 4 and edad <= 18 and edad >=0:
    print(f'El usuario debe pagar $5 por entrada.')
elif edad > 18 and edad >=0:
    print(f'El usuario debe pagar $10 por entrada.')
else:
    print(f'Edad inválida.')