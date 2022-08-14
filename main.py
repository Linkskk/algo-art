import random
import numpy as np
import matplotlib.pyplot as plt
from numerical_methods import Numerical 

numerical = Numerical()
methods = {"Newton": numerical.newton, "Steffensen": numerical.steffensen, 
            "Ostrowski": numerical.ostrowski, "Halley": numerical.halley}
test_function = random.choice(numerical.list)

def render(type, f, pixels=1000, xa=-1.5, xb=1.5, ya=-1.5, yb= 1.5):
    print(f"Generating {type}'s fractal...")
    x = np.linspace(xa, xb, pixels)
    y = np.linspace(ya, yb, pixels)
    xx, yy = np.meshgrid(x,y)
    z = xx + yy*1j
    im = np.frompyfunc(methods[type],2, 1)(z, f).astype(float)
    plt.imshow(im, cmap="magma")
    plt.axis("off")
    plt.grid(False)
    plt.savefig("test.png",bbox_inches='tight')
    plt.show()


x = input("Do you want to create a fractal? (y/n) \n")
if x.lower() == "y":
    print(f"Your function is: " + test_function["name"])
    y = input("Choose the method: (Newton/Ostrowski/Steffensen/Halley)\n")
    render(y, test_function["function"])



