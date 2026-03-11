# Pseudocódigo
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

# Linear Regression Toolkit 📊
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📖 Descripción
Este módulo proporciona herramientas robustas para el cálculo de regresiones lineales simples y estimaciones masivas. Desarrollado para la clase de Inteligencia Artificial, enfocado en código limpio, manejo de excepciones y logging profesional.

## 🚀 Características
- **Cálculo de Regresión:** Obtención de intercepto ($a$) y pendiente ($b$) mediante mínimos cuadrados.
- **Validación Automática:** Manejo de errores para dimensiones incompatibles o varianza cero.
- **Logging Integrado:** Registro de eventos para auditoría de modelos.
- **Type Hinting:** Código totalmente tipado para una mejor experiencia de desarrollo (DX).

## 🛠️ Instalación
Para usar esta biblioteca, clona el repositorio y asegúrate de tener las dependencias necesarias:

```bash
git clone [https://github.com/tu-usuario/nombre-repositorio.git](https://github.com/tu-usuario/nombre-repositorio.git)
cd nombre-repositorio
pip install -r requirements.txt

⚖️ Licencia

Este proyecto está bajo la Licencia MIT.

Consulta el archivo LICENSE para más detalles

