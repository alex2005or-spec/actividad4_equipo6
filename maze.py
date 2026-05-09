"""Maze, muévete de un lado a otro.

Ejercicios

1. Llevar la puntuación contando los clics.
2. Hacer el laberinto más difícil.
3. Generar el mismo laberinto dos veces.
"""

# Importa la función random para generar valores aleatorios.
from random import random

# Importa todas las funciones de turtle para dibujar en pantalla.
from turtle import *

# Importa la función line de freegames para dibujar líneas.
from freegames import line


def draw():
    """Dibuja el laberinto."""
    color('grey')    # Define el color de los muros del laberinto.
    width(6)         # Define el grosor de los muros del laberinto.

    # Recorre las posiciones en el eje x donde se dibujarán las líneas.
    for x in range(-200, 200, 40):

        # Recorre las posiciones en el eje y donde se dibujarán las líneas.
        for y in range(-200, 200, 40):

            # Decide aleatoriamente la dirección de cada muro.
            if random() > 0.5:
                # Dibuja una línea diagonal de abajo hacia arriba.
                line(x, y, x + 40, y + 40)
            else:
                # Dibuja una línea diagonal de arriba hacia abajo.
                line(x, y + 40, x + 40, y)

    # Actualiza la pantalla para mostrar el laberinto completo.
    update()


def tap(x, y):
    """Dibuja una línea y un punto cuando se hace clic en la pantalla."""

    # Si el clic está fuera del área del laberinto, levanta el lápiz.
    if abs(x) > 198 or abs(y) > 198:
        up()
    else:
        # Si el clic está dentro del área del laberinto, baja el lápiz para dibujar.
        down()

    width(3)         # Define el grosor del trazo que deja el jugador.
    color('purple')  # Define el color del trazo que deja el jugador.
    goto(x, y)       # Mueve el cursor a la posición donde se hizo clic.
    dot(8)           # Dibuja un punto en la posición del clic.


# Configura el tamaño y la posición de la ventana del juego.
setup(420, 420, 370, 0)

# Oculta la tortuga para que solo se vea el dibujo.
hideturtle()

# Desactiva la animación automática para dibujar más rápido.
tracer(False)

# Llama a la función que dibuja el laberinto.
draw()

# Detecta los clics del usuario y llama a la función tap.
onscreenclick(tap)

# Mantiene abierta la ventana del juego.
done()