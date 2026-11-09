# RETO SEMANA 5: Logica de bifurcacion
# Fundamentos de Python

# --- PRIMERA PARTE: Validar la palabra ---
print("--- VALIDADOR DE PALABRAS ---")
# Pedimos la palabra y quitamos los espacios que se puedan colar al inicio o final
palabra = input("Escribe una palabra: ").strip() 

# Usamos len() para sacar el número de letras
cantidad_letras = len(palabra)

# Evaluamos con if, elif y else
if cantidad_letras < 4:
    print("Hacen falta letras. Solo tiene", cantidad_letras, "letras.")
elif cantidad_letras > 8:
    print("Sobran letras. Tiene", cantidad_letras, "letras.")
else:
    # Si no es menor a 4 ni mayor a 8, está en el rango correcto
    print("¡Palabra correcta! Tiene", cantidad_letras, "letras.")


print("\n") # Esto es solo para dejar un espacio en la consola y que se vea ordenado


# --- SEGUNDA PARTE: Ubicar el cuadrante ---
print("--- DETECTOR DE CUADRANTES ---")
# Pedimos los dos números y usamos float() por si escriben decimales
x = float(input("Ingresa el valor de X: "))
y = float(input("Ingresa el valor de Y: "))

# Para que exista un cuadrante, ningún número puede ser exactamente 0
if x == 0 or y == 0:
    print("Error: Los números deben ser mayores o menores a cero (no pueden ser 0).")
else:
    # Ahora evaluamos los signos de X e Y
    if x > 0 and y > 0:
        print("El punto está en el Cuadrante I")
    elif x < 0 and y > 0:
        print("El punto está en el Cuadrante II")
    elif x < 0 and y < 0:
        print("El punto está en el Cuadrante III")
    elif x > 0 and y < 0:
        print("El punto está en el Cuadrante IV")