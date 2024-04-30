from interprete.cadenas import apply_rules, Interpreter

ω = "F-G-G"
π = {"F": "F-G+F+G-F", "G": "GG"}
interpreter = Interpreter ()
interpreter.t.penup()
interpreter.t.goto(-280, -280)
interpreter.t.pendown()
interpreter.execute(apply_rules(ω, π, 6), 120, 20)