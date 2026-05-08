"""
Simulaci¢n del Juego de la Vida.

El Juego de la Vida de Conway es un aut¢mata celular cl sico creado en 1970 por 
John Conway. https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
"""

from random import choice
from turtle import *
from freegames import square

# Diccionario principal que guarda el estado de cada celda (viva o muerta)
cells = {}
# Diccionario auxiliar para guardar el estado anterior y comparar "edades"
last_cells = {}

def initialize():
    """Inicializa las celdas de forma aleatoria."""
    # Primero, se establece un tablero vac¡o de -200 a 200 con celdas muertas (False)
    for x in range(-200, 200, 10):
        for y in range(-200, 200, 10):
            cells[x, y] = False

    # Luego, se llena el centro (-50 a 50) con estados aleatorios (viva/muerta)
    for x in range(-50, 50, 10):
        for y in range(-50, 50, 10):
            cells[x, y] = choice([True, False])

def step():
    """Calcula un paso (generaci¢n) en el Juego de la Vida."""
    global last_cells
    # Esto permite que la funci¢n draw identifique qu‚ c‚lulas son nuevas.
    last_cells = cells.copy()
    
    neighbors = {}

    # Se recorre la cuadr¡cula para contar los vecinos vivos de cada celda
    for x in range(-190, 190, 10):
        for y in range(-190, 190, 10):
            # Restamos el valor de la propia celda para contar solo los alrededores
            count = -cells[x, y]
            for h in [-10, 0, 10]:
                for v in [-10, 0, 10]:
                    count += cells[x + h, y + v]
            neighbors[x, y] = count

    # Aplicaci¢n de las reglas de evoluci¢n de Conway
    for cell, count in neighbors.items():
        if cells[cell]:
            # Muerte por soledad o sobrepoblaci¢n
            if count < 2 or count > 3:
                cells[cell] = False
        elif count == 3:
            # Nacimiento por reproducci¢n
            cells[cell] = True

def draw():
    """Dibuja las celdas procesando primero el color y luego el cuadrado."""
    step()   # Calculamos la nueva generaci¢n
    clear()  # Limpiamos el dibujo anterior
    
    for (x, y), alive in cells.items():
        # LOGICA DE COLOR: Determinamos el color antes de dibujar el cuadrado
        if alive:
            # Si estaba viva antes: Verde Oscuro. Si es nueva: Verde Claro.
            if last_cells.get((x, y), False):
                color_render = 'dark green'
            else:
                color_render = 'light green'
        else:
            # Si la celda est  muerta: Negro
            color_render = 'black'
            
        # CAMBIO SOLICITADO: El dibujo del cuadrado se ejecuta aqu¡
        # usando la variable color_render definida en el bloque anterior.
        square(x, y, 10, color_render)
        
    update()           # Refresca la pantalla
    ontimer(draw, 100) # Reitera el ciclo cada 100ms

# Configuraci¢n de la interfaz gr fica
setup(420, 420, 370, 0)
hideturtle()
tracer(False) 
initialize()
draw()
done()
