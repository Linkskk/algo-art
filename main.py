import PIL.Image as image
iterations = 100
max_error = 1e-3
h = 1e-3

coefficients = []
for i in range(9):
    response = int(input(f"Please enter the coefficient of the {8 - i}th power of the polynomial.\n"))
    coefficients.append(response)

#defining the function, f(x), and its derivative, q(x)
f = lambda x: coefficients[0]*x**8 + coefficients[1]*x**7 + coefficients[2]*x**6 \
              + coefficients[3]*x**5 + coefficients[4]*x**4 + coefficients[5]*x**3 + coefficients[6]*x**2 + \
              coefficients[7]*x**1 + coefficients[8]

q = lambda x: (f(x + complex(h,h)) - f(x))/ complex(h,h)
print("Generating the fractal....")


image_x = 500
image_y = 500
im = image.new(mode='RGB', size=(image_x, image_y))
pixels = im.load()

for x in range(image_x):
    for y in range(image_y):
        x0 = 2*(x - image_x)/ image_x + 1
        y0 = 2*(y - image_y)/ image_y + 1
        z = complex(x0, y0)
        for i in range(iterations):
            z0 = z - f(z) / q(z)
            if abs(z0 - z) < max_error:
                break
            z = z0
        im.putpixel((x,y), (255 - 10*i,255 - 10*i,255 - 10*i))

print("Here is your fractal!")
im.show()

