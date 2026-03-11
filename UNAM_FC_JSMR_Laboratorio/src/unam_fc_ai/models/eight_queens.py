import matplotlib.pyplot as plt
import time

'''ALGORITMO ResolverTodasLasReinas
    ENTRADA: tablero (lista), fila_actual, soluciones (lista de resultados)

    SI fila_actual == 8 ENTONCES
        AÑADIR copia de tablero A soluciones
        RETORNAR

    PARA cada columna DE 0 A 7 HACER
        SI EsPosicionSegura(tablero, fila_actual, columna) ENTONCES
            tablero[fila_actual] <- columna
            LLAMAR ResolverTodasLasReinas(tablero, fila_actual + 1, soluciones)
            # El "backtracking" ocurre aquí al probar la siguiente columna
            tablero[fila_actual] <- -1
    
FIN ALGORITMO

FUNCION EsPosicionSegura(tablero, fila, col)
    PARA cada fila_previa DE 0 A fila - 1 HACER
        distancia_filas <- fila - fila_previa
        distancia_cols <- ABS(col - tablero[fila_previa])
        
        # Si están en misma columna o misma diagonal
        SI tablero[fila_previa] == col O distancia_filas == distancia_cols ENTONCES
            RETORNAR Falso
    FIN PARA
    RETORNAR Verdadero
FIN FUNCION
'''

def es_seguro_optimizado(tablero, fila, columna):
    for i in range(fila):
        if tablero[i] == columna or abs(tablero[i] - columna) == abs(i - fila):
            return False
    return True

def resolver_reinas_completo(tablero, fila, soluciones):
    if fila == 8:
        soluciones.append(list(tablero))
        return

    for columna in range(8):
        if es_seguro_optimizado(tablero, fila, columna):
            tablero[fila] = columna
            resolver_reinas_completo(tablero, fila + 1, soluciones)
            tablero[fila] = -1

def dibujar_tablero(tablero, num_solucion):
    fig, ax = plt.subplots(figsize=(6, 6))
    # Crear el patrón de ajedrez (0 y 1 alternados)
    ajedrez = [[(i + j) % 2 for j in range(8)] for i in range(8)]
    
    ax.matshow(ajedrez, cmap="Greys", alpha=0.3)
    
    for fila, col in enumerate(tablero):
        ax.text(col, fila, '♛', va='center', ha='center', fontsize=30, color='darkblue')

    ax.set_title(f"Solución #{num_solucion}")
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()

# --- Ejecución ---
todas_las_soluciones = []
tablero_inicial = [-1] * 8

inicio = time.time()
resolver_reinas_completo(tablero_inicial, 0, todas_las_soluciones)
fin = time.time()

print(f"Análisis completado en {fin - inicio:.4f} segundos.")
print(f"Total de soluciones únicas encontradas: {len(todas_las_soluciones)}")

# Visualizar
for i in range(2):
    dibujar_tablero(todas_las_soluciones[i], i + 1)
