from interprete.cadenas import apply_rules, Interpreter

ω = "F"
π = {"F": "F[+F]F[-F[+F][-F]]F"}
interpreter = Interpreter ()
interpreter.t.left(135)
interpreter.execute(apply_rules(ω, π, 5), 29, 4)