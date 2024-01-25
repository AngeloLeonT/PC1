# Establecer un número entero positivo
# Verificar si el número establecido es positivo
# Obtener el resultado de la suma de los números enteros desde 1 hasta N: N*(N+1)//2 donde: N = numero
# Obtener el resultado final

numero = int(input("Ingrese un entero positivo N: "))

if numero <= 0:
    print("Por favor, ingrese un entero positivo.")
else:

    suma = numero * (numero + 1) // 2

    print(f"La suma de los enteros desde 1 hasta {numero} es: {suma}")