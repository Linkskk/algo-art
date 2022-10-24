import cmath as c
import numpy as np

class Numerical():


    def __init__(self):
        self.iterations = 100
        self.epsilon = 1e-5
        self.delta = 1e-8
        self.complex_delta = complex(self.delta, self.delta)
       
        #initalises a list of functions on which the root finding methods can work on
           
        self.list = [{"name": "(x^2)tanh(x) - 1", "function": lambda x: (x**2)*c.tanh(x) - 1}, 
        {"name": "cosh(x) - 1",  "function": lambda x: c.cosh(x) - 1},
        {"name": "cos(sin(x)) - π ",  "function": lambda x: c.cos(c.sin(x)) - c.pi},
        {"name": "(x^3)cos(x) - 1 ",  "function": lambda x: x**3 * c.cos(x) - 1},
        {"name": "(x^3+x^2+x)cos(sin(x))cos(x)^2-2", 
        "function": lambda x: (x**3 + x**2 + x)*c.cos(c.sin(x))*(c.cos(x)**2) - 2},
        {"name": "(x^2)arctan(x) - x^5 ",  "function": lambda x: x**2 * c.atan(x) - x**5}]
 
    
    def derivative(self, f, x):
        # finds the derivative of a function
        g = lambda x: (f(x + self.complex_delta) - f(x))/ self.complex_delta
        return g, g(x)
    

    def second_derivative(self, f, x):
        # finds the second derivative of a function
        g = self.derivative(f, x)[1]
        h = lambda x: (g(x + self.complex_delta) - g(x))/ self.complex_delta
        return h, h(x)

    def newton(self, x, f):
        
        for i in range(1, self.iterations + 1):
            try:
                dx = self.derivative(f, x)[1]
                if abs(dx) < self.epsilon:
                    break
                x0 = x - (f(x) / dx)
                if abs(f(x0)) < self.epsilon:
                    break
                x = x0
            except OverflowError:
                break
        return i

    def steffensen(self, x0, f):
        for i in range(1, self.iterations + 1):
            try:
                x1 = f(x0)
                x2 = f(x1)
                delta = x1 - x0
                delta_sqr = x0 - (2 * x1) + x2
                if abs(delta_sqr) < self.epsilon:
                    break
                aitkenX = x0 - ((delta ** 2) / delta_sqr)
                if abs(aitkenX - x2) < self.epsilon:
                    break
                x0 = aitkenX
            except OverflowError:
                break
        return i

    def ostrowski(self, x, f):
        for i in range(1, self.iterations + 1):
            try:
                dx = self.derivative(f, x)[1]
                if abs(dx) < self.epsilon:
                    break
                y0 = x - (f(x) / dx)
                difference = f(x) -2*f(y0)
                if abs(difference) < self.epsilon:
                    break
                x0 = y0 - f(y0)*(x - y0)/difference
                if abs(x0 - x) < self.epsilon:
                    break
                x = x0
            except OverflowError:
                break      
        return i

    def halley(self, x, f):
        for i in range(1, self.iterations + 1):
            try:
                dx = self.derivative(f, x)[1]
                ddx = self.derivative(f, x)[1]
                if abs(dx)<self.epsilon or abs(ddx) < self.epsilon:
                    break
                x0 = x - (2 * f(x) * dx) / (2 * (dx) ** 2 - f(x) * ddx)
                if abs(f(x0)) < self.epsilon:
                    break
                x = x0
            except OverflowError:
                break  
        return i

