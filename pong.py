"""Pong, juego cl sico de arcade.

Cambios realizados

1. Se cambi¢ el color de la pelota y las barras a azul.
2. Se cambi¢ el fondo a color negro.
"""

from random import choice, random
import turtle

from freegames import vector


def value():
    # Genera aleatoriamente la velocidad inicial de la pelota.
    return (3 + random() * 2) * choice([1, -1])


# Posici¢n inicial de la pelota.
ball = vector(0, 0)

# Direcci¢n y velocidad inicial de la pelota.
aim = vector(value(), value())

# Posici¢n vertical de cada jugador.
state = {1: 0, 2: 0}


def move(player, change):
    # Mueve la barra del jugador arriba y abajo.
    state[player] += change


def rectangle(x, y, width, height):
    # Dibuja un rect ngulo en la posici¢n indicada.
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()

    # Dibuja los lados del rect ngulo.
    for count in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()


def draw():
    # Dibuja el juego, mueve la pelota y revisa rebotes.
    turtle.clear()
    # Dibuja las barras de los jugadores.
    rectangle(-200, state[1], 10, 50)
    rectangle(190, state[2], 10, 50)
    # Mueve la pelota seg£n su direcci¢n actual.
    ball.move(aim)
    x = ball.x
    y = ball.y
    # Cambio visual: pelota y barras en color azul.
    turtle.up()
    turtle.goto(x, y)
    turtle.color("blue")
    turtle.dot(10)
    turtle.update()
    # Rebote de la pelota contra el borde superior e inferior.
    if y < -200 or y > 200:
        aim.y = -aim.y
    # Revisa si la pelota toca la barra izquierda.
    if x < -185:
        low = state[1]
        high = state[1] + 50
        if low <= y <= high:
            aim.x = -aim.x
        else:
            return
    # Revisa si la pelota toca la barra derecha.
    if x > 185:
        low = state[2]
        high = state[2] + 50
        if low <= y <= high:
            aim.x = -aim.x
        else:
            return
    # Ejecuta nuevamente la funci¢n para mantener el juego en marcha.
    turtle.ontimer(draw, 50)


# Configura el tama¤o y posici¢n de la ventana.
turtle.setup(420, 420, 370, 0)
# Cambio visual: fondo negro.
turtle.bgcolor("black")
# Oculta el cursor de dubujo.
turtle.hideturtle()
# Control manual de actualizaci¢n de pantalla.
turtle.tracer(False)
# Activa la lectura del teclado.
turtle.listen()
# Controles del jugador izquierdo.
turtle.onkey(lambda: move(1, 20), 'w')
turtle.onkey(lambda: move(1, -20), 's')
# Controles del jugador derecho.
turtle.onkey(lambda: move(2, 20), 'i')
turtle.onkey(lambda: move(2, -20), 'k')
# Inicia el juego.
draw()
# Mantiene abierta la ventana.
turtle.done()
