# Reto Semana 6: Validación y Ciclos
# Fundamentos de Python

print("=== VALIDADOR DE PALABRAS ===")
# Usamos un ciclo while infinito que se romperá (break) cuando la palabra sea correcta
while True:
    palabra = input("\nIngresa una palabra: ").strip()
    longitud = len(palabra)
    
    if longitud < 4:
        print("Error: Hacen falta letras. La palabra es muy corta. Intenta de nuevo.")
    elif longitud > 8:
        print("Error: Sobran letras. La palabra es muy larga. Intenta de nuevo.")
    else:
        print(f"¡Palabra correcta! Tiene {longitud} letras.")
        break # Si es correcta, salimos del ciclo y pasamos al siguiente programa


print("\n\n=== DETECTOR DE CUADRANTES CARTESIANOS ===")
# Ciclo para pedir coordenadas hasta que sean distintas de cero
while True:
    print("\n--- Ingresa las coordenadas ---")
    x = float(input("Valor de X: "))
    y = float(input("Valor de Y: "))
    
    # Validamos explícitamente el 0
    if x == 0 or y == 0:
        print("Error: Las coordenadas no pueden ser 0. Por favor, ingresa valores distintos a cero.")
        # Al no poner 'break', el ciclo vuelve a pedir los datos automáticamente
    else:
        # Si llega aquí, los datos son válidos. Evaluamos los cuadrantes.
        if x > 0 and y > 0:
            print("El punto se encuentra en el Cuadrante I")
        elif x < 0 and y > 0:
            print("El punto se encuentra en el Cuadrante II")
        elif x < 0 and y < 0:
            print("El punto se encuentra en el Cuadrante III")
        elif x > 0 and y < 0:
            print("El punto se encuentra en el Cuadrante IV")
        
        # Como ya dimos el resultado correcto, rompemos el ciclo para que el programa termine
        break 

print("\n¡Programa finalizado con éxito!")