import random
import numpy as np
import matplotlib.pyplot as plt
from newton import Numerical
from functions import functions_list
import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")


numerical = Numerical()
pixels=1000

#canvas 
xa=-2.5
xb=2.5
ya=-2.5
yb=2.5

##Inputs all of the points (pixels) into Newton's method. Each point is then assigned a colour according to the number of iterations
# required to converge to the nearest root. Finally, the points are plotted onto an grid/plane.

def render(data, function, address):
        print("Rendering art...")
        im = np.frompyfunc(numerical.newton,2, 1)(data, function).astype(float)
        fig = plt.figure(figsize=(1000 /200.0, 1000 / 200.0), dpi=200)
        ax = fig.add_axes([0, 0, 1, 1], aspect=1)
        ax.axis("off")
        ax.imshow(im, cmap="gist_heat")
        fig.savefig(address)


print("Welcome ^_^. My name is Pixel, your local robot artist!")
bot_is_on = True

while bot_is_on:
    art_request = input("Do you want me to make some art? If so, enter 'y'. If you want to change the settings, enter 's'. Otherwise, press 'n' to close\n")

    if art_request.lower() == "y":
        x = input("Great! Please enter the number of artworks you would like. \n")
        if int(x) > 0:
            for i in range(int(x)):
                test_function = random.choice(functions_list)
                print(f"Your function is: " + test_function["name"])
                #generates the points which are evenly spaced
                x = np.linspace(xa, xb, pixels)
                y = np.linspace(ya, yb, pixels)
                xx, yy = np.meshgrid(x,y)
                z = numerical.mobius(xx + yy*1j) if numerical.mobiusmode else xx + yy*1j
                render(z, test_function["function"], f"art{i}.png")
            print("I have created all the art requested. Enjoy! ^_^")

    #processes a change in the constants used in Newton's method, as well as configuring the Mobius transform
    if art_request.lower() == "s":
        alpha = input("Enter a new value for alpha: ")
        beta = input("Enter a new value for beta: ")
        mobius = input("Do you want to use the Mobius transform? Enter 'True' or 'False: ")
        numerical.settings(complex(alpha), complex(beta), bool(mobius.title()))

    if art_request.lower() == 'n':
        bot_is_on = False
    
