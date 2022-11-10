import numpy as np
import matplotlib.pyplot as plt
import cmath as c
import sys

iterations = 500
tolerance = 1e-10
delta = 1e-8

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")


def derivative(x, f):
    return (f(x + complex(delta, delta)) - f(x))/complex(delta, delta)

def newton(x, f):
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
    x = np.linspace(xa, xb, pixels)
    y = np.linspace(ya, yb, pixels)
    xx, yy = np.meshgrid(x,y)
    return xx + yy*1j

def render(function, address):
    data = generate_grid(1, -1, 1, -1, 1000)
    im = np.frompyfunc(newton,2, 1)(data, function).astype(float)
    fig = plt.figure(figsize=(1000 /200.0, 1000 / 200.0), dpi=500)
    ax = fig.add_axes([0, 0, 1, 1], aspect=1)
    ax.axis("off")
    ax.imshow(im, cmap="gist_gray")
    fig.savefig(address)



