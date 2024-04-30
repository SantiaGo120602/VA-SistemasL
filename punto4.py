import turtle as turtle
from interprete.cadenas import apply_rules, Interpreter

grammar = {"F": "F[+FF][-FF]F[-F][+F]F"}
ω = "F"

grammar2 = {
    "X": "X[-FFF][+FFF]FX",
    "Y": "YFX[+Y][-Y]"
    }
ω2 = "Y"

grammar3 = {
    "F": "FF+[+F-F-F]-[-F+F+F]",
    }
ω3 = "F"

grammar4 = {
    "F": "FF",
    "X": "F[+X]F[-X]+X"
    }
ω4 = "X"

cadenas = [apply_rules(ω, grammar, 3),
           apply_rules(ω2, grammar2, 4),
           apply_rules(ω3, grammar3, 3),
           apply_rules(ω4, grammar4, 6)]
deltas = [35, 25.7, 22.5, 20]
sizes = [10, 10, 8, 1]
colors = [(34, 139, 34),
          (0, 100, 0),
          (154, 205, 50),
          (165, 42, 42)]

interpreter = Interpreter(screen_width = 2000, screen_length = 2000)
interpreter.t.left(90)
#interpreter.execute_multiple(cadenas, deltas, sizes, colors=colors)
interpreter.generate_artificial_forest(cadenas, deltas, sizes, colors=colors)

