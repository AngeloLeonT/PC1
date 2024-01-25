# Establecer la cantidad de los payasos: peso: 112 g
# Establecer la cantidad de las muñecas: peso: 75 g
# Obtener el resultado

payasos = int(input("Ingrese la cantidad de payasos: "))
muñeca = int((input("Ingrese la cantidad de muñecas: ")))

peso_total = (payasos*112/1000)+(muñeca*75/1000)
print(f"El peso total de {payasos} payasos y {muñeca} muñecas es: {peso_total} kg")