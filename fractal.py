from matplotlib import pyplot as plt
from numerical_methods import Numerical
import numpy as np


class Fractal(Numerical):
    def __init__(self):
        super().__init__()
        self.pixels = 1000
        self.methods = {"Newton": self.newton, "Steffensen": self.steffensen,
                       "Ostrowski": self.ostrowski, "Halley": self.halley}
    
    def render(self, type, f, xa=-2.5, xb=2.5, ya=-2.5, yb=2.5):
        print(f"Generating {type}'s fractal...")
        x = np.linspace(xa, xb, self.pixels)
        y = np.linspace(ya, yb, self.pixels)
        xx, yy = np.meshgrid(x,y)
        z = xx + yy*1j
        im = np.frompyfunc(self.methods[type],2, 1)(z, f).astype(float)
        plt.imshow(im, cmap="magma")
        plt.axis("off")
        plt.grid(False)
        plt.savefig("test.png",bbox_inches='tight')
        plt.show()
    
