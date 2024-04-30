from interprete.cadenas import apply_rules, Interpreter

ω = "F+F+F+F"
π = {"F": "FF+F+F+F+FF"}
interpreter = Interpreter ()
interpreter.t.penup()
interpreter.t.goto(-240, 240)
interpreter.t.pendown()
interpreter.execute(apply_rules(ω, π, 5), 90, 2)