# Establecer nombre dle usuario
# Establecer la cantidad de shows musicales vistos en el último año
# Verificar si ha visto más de 3 shows en el último año
# Presentar respuesta

nombre_de_usuario = input("Ingrese nombre de usuario: ")
shows_vistos = int(input("Ingrese la cantidad de shows musicales vistos en el último año: "))

if shows_vistos > 3:
    print(f"El usuario {nombre_de_usuario} ha visto más de 3 shows en el último año.")
else:
    print(f"El usuario {nombre_de_usuario} no ha visto más de 3 shows en el último año.")


