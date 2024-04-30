from interprete.cadenas import apply_rules, Interpreter

ω = "G"
π = {"F": "FF", "G": "FG[-F[G]-G][G+G][+F[G]+G]"}
interpreter = Interpreter ()
interpreter.t.left(90)
interpreter.execute(apply_rules(ω, π, 5), 22.5, 20)