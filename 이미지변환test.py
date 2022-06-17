import numpy as np
from PIL import Image

#array = np.arange(0, 737280, 1, np.uint8)
#array = np.reshape(array, (1024, 720))

array = np.random.randint(1, 737280, (255,255))

im = Image.fromarray(array)
im.save("test1.png")

