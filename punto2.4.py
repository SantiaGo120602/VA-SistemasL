from interprete.cadenas import apply_rules, Interpreter

ω = "F-F-F-F"
π = {"F": "F-F+F+FF-F-F+F"}
interpreter = Interpreter ()
interpreter.execute(apply_rules(ω, π, 5), 90, 2)