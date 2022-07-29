import PIL.Image as image

h = complex(1e-3, 1e-3)
iterations = 100
limit = 1e-6


class Fractal():

    def __init__(self, function):
        self.function = function
        self.derivative = lambda x: (self.function(x + h) - self.function(x)) / h
        self.image_x = 1000
        self.image_y = 1000
        self.image = image.new(mode='RGB', size=(self.image_x, self.image_y))
        self.pixels = self.image.load()

    def interpolate_value(self, x, y):
        x0 = (2 * (x - self.image_x) / self.image_x) + 1
        y0 = (2 * (y - self.image_y) / self.image_y) + 1
        z = complex(x0, y0)
        return z

    def newton(self, x):
        count = 0
        for i in range(iterations):
            x0 = x - (self.function(x) / self.derivative(x))
            count += 1
            if abs(x0 - x) < limit:
                break
            x = x0
        return x, count

