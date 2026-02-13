import turtle
import math
import random

s = turtle.Screen()
s.setup(800, 800)
s.bgcolor("black")
s.tracer(0)

t = turtle.Turtle()
t.hideturtle()

def obtener_punto_corazon(t_param, escala):
    x = 16 * math.sin(t_param)**3
    y = 13 * math.cos(t_param) - 5 * math.cos(2*t_param) - 2 * math.cos(3*t_param) - math.cos(4*t_param)
    return x * escala, y * escala

particulas = []
for _ in range(800):
    theta = random.uniform(0, 2 * math.pi)
    variacion = random.uniform(0.8, 1.2)
    particulas.append((theta, variacion))

def animar(tiempo):
    t.clear()
    latido = 15 + math.sin(tiempo) * 2

    for theta, var in particulas:
        x, y = obtener_punto_corazon(theta, latido * var)
        t.penup()
        t.goto(x, y)
        t.color("blue")
        t.dot(random.randint(1, 3))

        s.update()
        s.ontimer(lambda: animar(tiempo + 0.15), 10)

animar(0)
turtle.done()