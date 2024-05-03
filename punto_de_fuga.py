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
tk.mainloop()