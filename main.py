from fractal import Fractal

f = lambda x: x**3 - 1

fractal = Fractal(f)
darkness = 10

print("Generating fractal...")
for x in range(fractal.image_x):
    for y in range(fractal.image_y):
        z = fractal.interpolate_value(x,y)
        z0, c = fractal.newton(z)
        fractal.image.putpixel((x,y), (255 - darkness * c,) * 3)

fractal.image.show()

