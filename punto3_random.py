from interprete.cadenas import apply_rules, Interpreter

grammar = {
    "F": "FF+[+F-F-F]-[-F+F+F]",
    }
ω = "F"

interpreter = Interpreter ()
interpreter.t.left(90)
interpreter.execute_with_random(apply_rules(ω, grammar, 4), 25.7, 10)
