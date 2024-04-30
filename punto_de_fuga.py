from interprete.cadenas import apply_rules, Interpreter



ω = "[x-]y"
π = {"x": "FFFx",
     "y": "FFFy"}
interpreter = Interpreter (1900, 1900)
interpreter.t.setheading(248)
interpreter.t.fillcolor("black") 
interpreter.t.begin_fill()
interpreter.t.circle(4)
interpreter.t.end_fill()
print(apply_rules(ω, π, 12))
interpreter.t._tracer(1)
interpreter.execute(apply_rules(ω, π, 4), 45, 100)