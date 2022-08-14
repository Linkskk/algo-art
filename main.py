from fractal import Fractal
import random


fractal = Fractal()
list_of_functions = fractal.list
function = random.choice(list_of_functions)


x = input("Do you want to create a fractal? (y/n) \n")
if x.lower() == "y":
    print(f"Your function is: " + function["name"])
    y = input("Choose the method: (Newton/Ostrowski/Steffensen/Halley)\n")
    fractal.render(y, function["function"])

