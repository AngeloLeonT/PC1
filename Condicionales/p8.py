# Establecer la cadena hora a horas y minutos
# Establecer si es desayuno, almuerzo o cena
# Validar hora dle usuario
# Obtener el resultado

def verificar_hora_comida(hora):

    horas, minutos = map(int, hora.split(':'))

    if 7 <= horas < 8 or (horas == 8 and minutos == 0):
        return "Es hora de desayunar."
    elif 12 <= horas < 13 or (horas == 13 and minutos == 0):
        return "Es hora de almorzar."
    elif 18 <= horas < 19 or (horas == 19 and minutos == 0):
        return "Es hora de cenar."
    else:
        return None

hora_usuario = input("Introduce la hora en formato de 24 horas (por ejemplo, 14:30): ")

resultado = verificar_hora_comida(hora_usuario)

if resultado:
    print(resultado)
else:
    print("No es hora de comer en este momento.")