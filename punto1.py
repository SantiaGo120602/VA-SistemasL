from interprete.cadenas import apply_rules, Interpreter

axiom = 'FX'
production_rules = {"X": "X+YF", "Y": "FX-Y"}

new_axiom = apply_rules(axiom, production_rules, 10)
interpreter = Interpreter()
interpreter.t.left(90)
interpreter.execute(new_axiom, 90, 10)

