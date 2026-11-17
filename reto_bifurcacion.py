
# ==========================================
# RETO SEMANAL - LOGICA DE BIFURCACION
# ==========================================

# Funcion 1: Validar longitud de una palabra

def validar_palabra():

    palabra = input("Ingresa una palabra: ").strip()

    longitud = len(palabra)

    if longitud < 4:
        print("Palabra incorrecta: Tiene menos de 4 letras.")

    elif longitud > 8:
        print("Palabra incorrecta: Tiene mas de 8 letras.")

    else:
        print("Palabra correcta: Tiene entre 4 y 8 letras.")



# Funcion 2: Determinar el cuadrante cartesiano

def determinar_cuadrante():

    x = float(input("Ingresa el valor de X: "))
    y = float(input("Ingresa el valor de Y: "))

    if x > 0 and y > 0:
        print("El punto se encuentra en el cuadrante I.")

    elif x < 0 and y > 0:
        print("El punto se encuentra en el cuadrante II.")

    elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III.")

    elif x > 0 and y < 0:
        print("El punto se encuentra en el cuadrante IV.")

    else:
        print("El punto se encuentra sobre un eje o en el origen.")


# ==========================================
# EJECUCION DEL PROGRAMA
# ==========================================

print("\n--- VALIDACION DE PALABRA ---")
validar_palabra()

print("\n--- UBICACION EN EL PLANO CARTESIANO ---")
determinar_cuadrante()

print("\nPrograma finalizado correctamente.")
