from interprete.cadenas import apply_rules, Interpreter
import tkinter as tk




interpreter = Interpreter(1900, 1900)
interpreter.t.setheading(250)
interpreter.screen.bgcolor("black")
grammar4 = {
    "F": "FF",
    "X": "F[+X]F[-X]+X"
    }
ω4 = "X"


for i in range(1, 8):
    #rgb(241,101,102)
    interpreter.t.penup()
    interpreter.t.goto(0, 1_020)
    interpreter.t.pendown()
    interpreter.t.setheading(250)
    interpreter.t.color(203,222,126)
    ω = "[x++++Y++++][x----Y"
    π = {"x": "F" * (16 * i),
    "X": "X[-FFF][+FFF]FX",
    "Y": "YFX[+Y][-Y]"}
    interpreter.execute(apply_rules(ω, π, 4), 40, 4 * i, showing=False, forest_color=True)

interpreter.t.penup()
interpreter.t.goto(0, 1_020)
interpreter.t.pendown()
interpreter.t.setheading(250)

def draw_triangle(x1, y1, x2, y2, x3, y3, color):
    interpreter.t.penup()
    interpreter.t.goto(x1, y1)
    interpreter.t.pendown()
    interpreter.t.fillcolor(color)
    interpreter.t.begin_fill()
    interpreter.t.goto(x2, y2)
    interpreter.t.goto(x3, y3)
    interpreter.t.goto(x1, y1)
    interpreter.t.end_fill()

x1, y1 = 0, 1020
x2, y2 = -735, -1_000
x3, y3 = 735, -1_000
triangle_color = (117,104,121)
draw_triangle(x1, y1, x2, y2, x3, y3, triangle_color)

x1, y1 = 0, 1020
x2, y2 = -600, -1_000
x3, y3 = 600, -1_000
triangle_color = (119,124,129)
draw_triangle(x1, y1, x2, y2, x3, y3, triangle_color)

x1, y1 = 0, 1020
x2, y2 = -500, -1_000
x3, y3 = 500, -1_000
triangle_color = (89,84,125)
draw_triangle(x1, y1, x2, y2, x3, y3, triangle_color)
tk.mainloop()