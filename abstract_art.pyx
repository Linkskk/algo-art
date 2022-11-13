import numpy as np
import matplotlib.pyplot as plt
import cmath as c
import sys

iterations = 500 (#iterations limit)
tolerance = 1e-10
delta = 1e-8

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")


def derivative(x, f):
    # Calculates the derivative of a given function at a specified point
    return (f(x + complex(delta, delta)) - f(x))/complex(delta, delta)

def newton(x, f):
    # Applies the Newton Raphson method for a fixed number of iterations at a specified point in the complex plane. There are two possible cases:    
    # 1 -  process converges at a point - return required number of iterations, which is less than or equal to the iterations limit   
    # 2 -  process doesn't converge - we either diverge to ± infinity, or oscillate between points indefinitelty - return iterations limit    
    cdef int i
    for i in range(iterations):
        try:
            dx = derivative(x, f)
            if abs(dx) < tolerance:
                break
            x0 = x - (f(x) / dx)
            if abs(f(x0)) < tolerance:
                break
            x = x0
            
        except OverflowError:
            break        
    return i

def steffensen(x0, f):
    # Applies Steffenson's method for a fixed number of iterations at a specified point, returning the number of iterations 
    # Aitken's delta squared process is used to accelerate convergence    
    cdef int i
    for i in range(iterations):
        try:
            x1 = f(x0)
            x2 = f(x1)
            delta = x1 - x0
            delta_sqr = x0 - (2 * x1) + x2
            if abs(delta_sqr) < tolerance:
                break
            aitkenX = x0 - ((delta ** 2) / delta_sqr)
            if abs(aitkenX - x2) < tolerance:
                break
            x0 = aitkenX
        except OverflowError:
            break
    return i


def generate_grid(double xa, double xb, double ya, double yb, int pixels):
    #generates the complex plane   
    x = np.linspace(xa, xb, pixels)
    y = np.linspace(ya, yb, pixels)
    xx, yy = np.meshgrid(x,y)
    return xx + yy*1j

def render(function, address):
    # creates a piece of art by assigning colors based on the number of iterations returned from the applied method
    data = generate_grid(1, -1, 1, -1, 1000)
    im = np.frompyfunc(newton,2, 1)(data, function).astype(float)
    fig = plt.figure(figsize=(1000 /200.0, 1000 / 200.0), dpi=500)
    ax = fig.add_axes([0, 0, 1, 1], aspect=1)
    ax.axis("off")
    ax.imshow(im, cmap="gist_gray")
    fig.savefig(address)



