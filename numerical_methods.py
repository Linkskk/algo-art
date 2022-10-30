import cmath as c
import numpy as np

ITERATIONS = 200
EPSILON = 1e-5
DELTA = 1e-8


class Numerical():

    def __init__(self):
        self.alpha = 1
        self.gamma = 0
        self.mobiusmode = False
        self.functions = \
            [
            {"name": "(x^2)tanh(x) - 1", "function": lambda x: (x**2)*c.tanh(x) - 1}, 
            {"name": "cosh(x) - 1",  "function": lambda x: c.cosh(x) - 1},
            {"name": "cos(sin(x)) - π ",  "function": lambda x: c.cos(c.sin(x)) - c.pi},
            {"name": "(x^3)cos(x) - 1 ",  "function": lambda x: x**3 * c.cos(x) - 1},
            {"name": "(x^3+x^2+x)cos(sin(x))cos(x)^2-2", "function": lambda x: (x**3 + x**2 + x)*c.cos(c.sin(x))*(c.cos(x)**2) - 2},
            {"name": "(x^2)arctan(x) - x^5 ",  "function": lambda x: x**2 * c.atan(x) - x**5},
            {"name": "x^3 - 1 ",  "function": lambda x: x**3 - 1},
            {"name": "(x^2)ln(x) - 5",  "function": lambda x: (x**2)*c.log(x) - 5},
            {"name": "x^8 - 1",  "function": lambda x: x**8 - x**4 - 1},
            {"name": "i^x - 1",  "function": lambda x: (0 + 1j)**x - 1},
            {"name": "tanh(xlog(x))",  "function": lambda x: c.tanh(x*c.log(x))},
            {"name": "x^x - 1",  "function": lambda x: x**x - 1},
            {"name": "x^20 - 1",  "function": lambda x: x**20 - 1}           
            ]

    #returns either the derivative of a function or the value of the derivative at a specified point
    def derivative(self, f, x):
        g = lambda x: (f(x + complex(DELTA, DELTA)) - f(x))/ complex(DELTA, DELTA)
        return g, g(x)

    def newton(self, x, f):
        count = 0
        for i in range(ITERATIONS):
            try:
                dx = self.derivative(f, x)[1]
                if abs(dx) < EPSILON:
                    break
                x0 = x - self.alpha*(f(x) / dx) + self.gamma
                if abs(f(x0)) < EPSILON:
                    break
                x = x0
            except OverflowError:
                break        
        return i


    def mobius(self, x, a = 0, b = -1, c = 1, d = 1):
        return (a*x + b) / (c*x + d)

    #allows the user to change the parameters used in Newton's method
    def settings(self, alpha, mobius , gamma):
        self.alpha = alpha
        self.gamma = gamma
        self.mobiusmode = mobius

