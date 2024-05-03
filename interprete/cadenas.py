import turtle
import tkinter as tk
from random import randrange, randint

def apply_rules(
        axiom: str, production_rules: dict[str, str],
        iterations: int) -> str:
    if iterations == 0:
        return axiom
    
    new_axiom = ""
    for character in axiom:
        if character in production_rules:
            new_axiom += production_rules[character]
            if iterations == 1:
                random_add = randint(1, 200)
                if (random_add < 40):
                    new_axiom += "P"
                if (random_add > 180):
                    new_axiom += "FFFF"
        else:
           new_axiom += character
    return apply_rules(new_axiom, production_rules, iterations-1)

class Interpreter:
    def __init__(self, screen_width: int = 9000, screen_length: int = 9000) -> None:
        self.root = tk.Tk()
        #self.root.geometry('500x500-5+40')
        self.cv = turtle.ScrolledCanvas(self.root, width=1900, height=900)
        self.cv.pack()
        self.screen = turtle.TurtleScreen(self.cv)
        self.screen.screensize(screen_width, screen_length)
        self.screen.colormode(255)
        self.t = turtle.RawTurtle(self.screen)
        self.t.hideturtle()
        self.t._tracer(0)
        self.t.width(2)
        self.posible_positions: list[tuple[int]] = [(x, y) for x in range(-(screen_width//2) + 200, (screen_width//2) - 200, 200) for y in range(-(screen_length//2) + 200, (screen_length//2) - 200, 400)]
        self.position_queue: list[turtle.Vec2D] = []
        self.move_dict = {"F": self.t.forward, "G": self.t.forward}
        self.rotate_dict = {"-": self.t.left, "+": self.t.right}
        self.change_dict = {"[": self.save_last_postition, "]": self.go_to_last_position}

    def execute_with_random(
            self, cadena: str, delta: float,
            size: float, showing: bool =True) -> None:
        for c in cadena:
            if c in self.move_dict:
                for i in range(randint(1, 2)):
                    self.move_dict[c](size)
            elif c in self.rotate_dict:
                prob = randint(1, 7)
                if prob >= 6:
                    self.rotate_dict[c](delta + randint(-2, 2))    
                else:
                    self.rotate_dict[c](delta)
            elif c in self.change_dict:
                self.change_dict[c]()
        if showing:
            tk.mainloop()

    def execute(
                self, cadena: str,
                delta: float, size: float,
                showing: bool = True,
                forest_color: bool = False) -> None:
        for c in cadena:
            if c == "P":
                self.t.color(246,40,25)
                self.t.fillcolor(246,40,25)
                self.t.begin_fill() 
                self.t.circle(3)
                self.t.end_fill()
                self.t.color(203,222,126)
            if c in self.move_dict:
                self.move_dict[c](size)
            elif c in self.rotate_dict:
                self.rotate_dict[c](delta)
            elif c in self.change_dict:
                self.change_dict[c]()
        if showing:
            tk.mainloop()
    
    def execute_multiple(
            self, cadenas: list[str], deltas: list[float],
            sizes: list[float], randomness: bool = True,
            colors: tuple[tuple[int]] = None,
            showing: bool = True,
            random_positions: bool = False) -> None:
        if not random_positions:
            in_x, in_y = tuple(self.t.pos())
        for i, (c, d, s) in enumerate(zip(cadenas, deltas, sizes)):
            if random_positions:
                in_x, in_y = self.posible_positions.pop(randrange(len(self.posible_positions)))
            else:
                in_x+=300
            self.t.color(colors[i])
            self.t.penup()
            self.t.goto(in_x, in_y)
            self.t.pendown()
            if randomness:
                self.execute_with_random(c, d, s, False)
            else:
                self.execute(c, d, s, False)
            
            self.t.setheading(90)
        if showing:
            tk.mainloop()

    def generate_artificial_forest(
            self, cadenas: list[str], deltas: list[float],
            sizes: list[float], randomness: bool = True,
            colors: tuple[tuple[int]] = None,
            showing: bool = True,
            iterations: int = 5) -> None:
        self.screen.bgcolor((152, 251, 152))
        for _ in range(iterations):
            self.execute_multiple(cadenas, deltas, sizes, colors=colors, showing=False, random_positions = True, randomness=randomness)
        if showing:
            tk.mainloop()

    def generate_vanishing_point():
        pass

    def go_to_last_position(self) -> None:
        self.t.penup()
        self.t.goto(tuple(self.position_queue.pop()))
        self.t.pendown()

    def save_last_postition(self) -> None:
        self.position_queue.append(self.t.position())

       


