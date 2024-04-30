from interprete.cadenas import apply_rules, Interpreter

ω = "F"
π = {"F": "F+F--F+F"}
interpreter = Interpreter ()
interpreter.execute(apply_rules(ω, π, 8), 60, 2)