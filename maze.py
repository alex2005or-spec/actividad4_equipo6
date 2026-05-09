"""Maze, muévete de un lado a otro.

Ejercicios

1. Llevar la puntuación contando los clics.
2. Hacer el laberinto más difícil.
3. Generar el mismo laberinto dos veces.
"""

# Importa la función random para generar valores aleatorios.
from random import random

# Importa el módulo turtle para dibujar en pantalla.
import turtle

# Importa la función line de freegames para dibujar líneas.
from freegames import line


def draw():
    """Dibuja el laberinto."""

    # Define el color de los muros del laberinto.
    turtle.color("grey")

    # Define el grosor de los muros del laberinto.
    turtle.width(6)

    # Recorre las posiciones horizontales.
    for x in range(-200, 200, 40):

        # Recorre las posiciones verticales.
        for y in range(-200, 200, 40):

            # Decide aleatoriamente la dirección de la línea.
            if random() > 0.5:

                # Dibuja una línea diagonal ascendente.
                line(x, y, x + 40, y + 40)
            else:

                # Dibuja una línea diagonal descendente.
                line(x, y + 40, x + 40, y)

    # Actualiza la pantalla con el laberinto generado.
    turtle.update()


def tap(x, y):
    """Dibuja una línea y un punto cuando se hace clic."""

    # Verifica si el clic está fuera de los límites.
    if abs(x) > 198 or abs(y) > 198:

        # Levanta el lápiz para no dibujar fuera del área.
        turtle.up()
    else:

        # Baja el lápiz para permitir el dibujo.
        turtle.down()

    # Define el grosor del trazo del usuario.
    turtle.width(3)

    # Define el color del trazo del usuario.
    turtle.color("purple")

    # Mueve el cursor a la posición seleccionada.
    turtle.goto(x, y)

    # Dibuja un punto en la posición del clic.
    turtle.dot(8)


# Configura el tamaño y posición de la ventana.
turtle.setup(420, 420, 370, 0)

# Oculta el cursor de turtle.
turtle.hideturtle()

# Desactiva la animación automática.
turtle.tracer(False)

# Llama a la función que dibuja el laberinto.
draw()

# Detecta clics y ejecuta la función tap.
turtle.onscreenclick(tap)

# Mantiene abierta la ventana del programa.
turtle.done()
