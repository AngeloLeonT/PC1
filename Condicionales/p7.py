# Establecer los números
# Establecer las opciones que se elegirán

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

while(True):
    print("""¿Qué quieres hacer? Escribe una opción
    1) Suma de dos número
    2) Resta de dos número
    3) Multiplicación de dos números""")
    opcion = input()
    if opcion == '1':
        print(f'el resultado de la suma es {num1+num2}')
        break
    elif opcion == '2':
        print(f'El resultado de la resta es {num1-num2}')
        break
    elif opcion =='3':
        print(f'El resultado de la multiplicación es {num1*num2}')
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")
        break