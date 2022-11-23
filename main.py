import abstract_art
import time
import cmath as c

st = time.time()
abstract_art.render("art.png")
et = time.time()

print(f"Time to create art: {et - st} seconds")
