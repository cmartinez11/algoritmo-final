def ordenar_calificaciones_insercion(calificaciones):
    
    #Resuelve el problema de ordenar las calificaciones de los estudiantes del colegio Fe y Alegría 10 utilizando el algoritmo de Inserción.
    
    if not calificaciones:
        raise ValueError("El conjunto de calificaciones no puede estar vacío.")
    
    # Validar rango de notas escolares (0 a 20)
    for nota in calificaciones:
        if not (0 <= nota <= 20):
            raise ValueError(f"La calificación {nota} está fuera del rango permitido (0-20).")

    arr = list(calificaciones)
    n = len(arr)
    
    # Algoritmo de Inserción
    for i in range(1, n):
        clave = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = clave
        
    return arr

if __name__ == "__main__":
    # Notas desordenadas de un aula del colegio Fe y Alegría 10
    notas_bimestrales = [14, 5, 18, 12, 20, 11, 8, 16, 13, 21, 9, 15]
    
    print("========================================================")
    print("  SISTEMA DE ORDENAMIENTO DE NOTAS - FE Y ALEGRÍA 10    ")
    print("========================================================")
    print(f"Notas ingresadas (Desordenadas): {notas_bimestrales}")
    
    notas_ordenadas = ordenar_calificaciones_insercion(notas_bimestrales)
    
    print(f"Notas procesadas (Ordenadas)  : {notas_ordenadas}")
    print("¡Proceso completado con éxito para el registro oficial!")