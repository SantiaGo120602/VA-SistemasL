from interprete.cadenas import apply_rules, Interpreter

ω = "F"
π = {"F": "FF+[+F-F-F]-[-F+F+F]"}
interpreter = Interpreter ()
interpreter.t.left(90)
interpreter.execute(apply_rules(ω, π, 4), 22.5, 8)