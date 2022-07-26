import PIL.Image as image
import cmath
import random

f = lambda x: x ** 3 - 1


def newton(z, f, max_iter=100, t=1e-6):
    h = 0.00001
    for i in range(max_iter):
        step = h * f(z) / (f(z + h) - f(z))
        if abs(step) < t:
            return z
        z -= step
    return z


def pixel_color(point, roots, colors):
    c = roots[0]
    for i in range(len(roots)):
        if abs(point - roots[i]) < abs(c):
            c = roots[i]
    return colors[roots.index(c)]


roots = [cmath.rect(1, i * cmath.pi / 3) for i in range(3)]
colors = [(0,0,0), (255,250,240), (255,255,255)]

image_size = 10000
half_size = image_size // 2
im = image.new(mode='RGB', size=(image_size, image_size))
pixels = im.load()

for i in range(image_size):
    for j in range(image_size):
        i0 = (i - half_size) / half_size
        j0 = (j - half_size) / half_size
        point = complex(i0, j0)
        counter = newton(point, f)
        c = pixel_color(counter, roots, colors)
        pixels[i, j] = c

im.show()
