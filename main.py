import abstract_art
import time
import cmath as c

test_function = lambda x: c.cos(c.sin(x)) - c.pi
st = time.time()
abstract_art.render(test_function, "abstract_art.png")
et = time.time()

print(f"Time to create art: {et - st} seconds")
