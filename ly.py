import turtle
import time

ventana = turtle.Screen()
ventana.setup(width=700, height=600)
ventana.bgcolor("black")
ventana.title("Kirby's Special Message")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

AZUL_RETRO = "#00FFFF"
ROSADO_KIRBY = "#FFB7C5"

def escribir_texto(mensaje, y_offset=-200, fuente=14):
    t.penup()
    t.goto(0, y_offset)
    t.color(AZUL_RETRO)
    t.write(mensaje, align="center", font=("Courier", fuente, "bold"))

def dibujar_kirby():
    t.clear()
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.color(ROSADO_KIRBY)
    t.begin_fill()
    t.circle(80)
    t.end_fill()
    t.color("black")
    for x in [-25, 25]:
        t.penup()
        t.goto(x, 40)
        t.pendown()
        t.pensize(5)
        t.forward(1) # Un punto grueso
    # Mejillas
    t.pensize(1)
    t.color("#FF69B4")
    for x in [-45, 45]:
        t.penup()
        t.goto(x, 20)
        t.begin_fill()
        t.circle(10)
        t.end_fill()
    # Boca pequeña
    t.penup()
    t.goto(-10, 10)
    t.pendown()
    t.color("black")
    t.setheading(-60)
    t.circle(12, 120)

def secuencia_dialogos():
    escribir_texto("KIRBY ADVENTURE: VALENTINE EDITION", 50, 20)
    escribir_texto("Presiona ENTER para continuar...", -50, 12)
    ventana.textinput("Inicio", "Presiona Enter o escribe algo para comenzar")
    t.clear()
    
    dibujar_kirby()
    
    mensajes = [
        ("Hola...", 2),
        ("Adios", 2)
    ]
    for m, espera in mensajes:
        escribir_texto(m)
        time.sleep(espera)
        t.clear()
        dibujar_kirby()

    t.clear()
    ventana.bgcolor("black")
    time.sleep(1.5)

    dibujar_kirby()
    dialogos_largos = [
        "Es broma",
        "Ahora si, hola, trabaje un poco en esto porque\no es algo que suelo hacer.",
        "Bueno, es algo que realmente nunca hice",
        "Que raro TT",
        "Dios, me siento melosa haciendo esto...",
        "Bueño",
        "Vamos a casarnos en la estación espacial",
        "Aceptas si o no?"
    ]
    for d in dialogos_largos:
        escribir_texto(d)
        time.sleep(3)
        t.clear()
        dibujar_kirby()

    decision()

def decision():
    t.clear()
    dibujar_kirby()
    escribir_texto("¿ACEPTAS?", 150)
    respuesta = ventana.textinput("LA ESTACIÓN ESPACIAL", "Escribe 'SI' o 'NO':")

    if respuesta and (respuesta.lower() == "si" or respuesta.lower() == "acepto"):
        ventana.bgcolor("black")
        t.clear()
        t.penup()
        t.goto(0, 50)
        t.color(AZUL_RETRO)
        t.write("⏳", align="center", font=("Arial", 60, "normal"))
        escribir_texto("Creating new world...", -50, 18)

    else:
        ventana.bgcolor("black")
        t.clear()
        t.penup()
        t.goto(0, 0)
        t.color("red")
        t.write("GAME OVER", align="center", font=("Courier", 60, "bold"))

secuencia_dialogos()
ventana.mainloop()