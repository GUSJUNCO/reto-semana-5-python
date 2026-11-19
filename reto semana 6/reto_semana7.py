# ==========================================
# Reto Semanal - Semana 7
# Optimización con Colecciones
# ==========================================

def ejecutar_reto():
    print("¡Bienvenido al Reto de la Semana 7!\n")

    # -------------------------------------------------------------------------
    # INSTRUCCIÓN 1: Crear una lista para almacenar las palabras intentadas.
    # TIPO DE COLECCIÓN: Lista (list).
    # Explicación: Una lista es una colección ordenada y MUTABLE (podemos 
    # agregar o quitar elementos). Ideal para guardar un historial dinámico.
    # -------------------------------------------------------------------------
    historial_palabras = []
    
    print("--- PARTE 1: Registro de Palabras ---")
    # Simularemos que el usuario ingresa 3 palabras para llenar la lista
    for i in range(3):
        palabra = input(f"Ingresa la palabra #{i+1}: ")
        
        # Agregamos la palabra a la lista usando el método .append()
        historial_palabras.append(palabra)
        
        # (Opcional) Mantenemos la lógica de la semana 5 para que el código sirva de algo
        longitud = len(palabra)
        if 4 <= longitud <= 8:
            print(f"  -> '{palabra}' es correcta.")
        else:
            print(f"  -> '{palabra}' no cumple con la longitud de 4 a 8 letras.")

    # Mostramos la lista completa
    print(f"\n[LISTA] Las palabras guardadas son: {historial_palabras}\n")


    # -------------------------------------------------------------------------
    # INSTRUCCIÓN 2: Usar una tupla para definir nombres de cuadrantes.
    # TIPO DE COLECCIÓN: Tupla (tuple).
    # Explicación: Una tupla es una colección ordenada e INMUTABLE (no se puede 
    # modificar). Es perfecta para datos fijos, como los nombres de los ejes.
    # -------------------------------------------------------------------------
    print("--- PARTE 2: Nombres de Cuadrantes ---")
    
    nombres_cuadrantes = ("Cuadrante I", "Cuadrante II", "Cuadrante III", "Cuadrante IV")
    
    # ACCESO MEDIANTE ÍNDICES (Instrucción 2):
    # En Python los índices empiezan en 0. 
    print(f"Accediendo por índice [0]: {nombres_cuadrantes[0]}")
    print(f"Accediendo por índice [1]: {nombres_cuadrantes[1]}")
    print(f"Accediendo por índice [2]: {nombres_cuadrantes[2]}")
    print(f"Accediendo por índice [3]: {nombres_cuadrantes[3]}\n")

    # EXTRA (Para cumplir con "almacenar resultados" del Entregable):
    # Usaremos un diccionario para asociar un índice de la tupla con un mensaje.
    # TIPO DE COLECCIÓN: Diccionario (dict). Guarda pares Clave-Valor.
    registro_cuadrantes = {}
    
    # Llenamos el diccionario de forma automática
    for i in range(len(nombres_cuadrantes)):
        # La clave será el nombre del cuadrante, el valor será un mensaje
        registro_cuadrantes[nombres_cuadrantes[i]] = f"Este es el índice {i} de la tupla"
        
    print(f"[DICCIONARIO] Resultados almacenados: {registro_cuadrantes}")


# Ejecutamos el programa
if __name__ == "__main__":
    ejecutar_reto()