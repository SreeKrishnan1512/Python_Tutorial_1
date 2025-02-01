from matplotlib import pyplot as plt

import math
import numpy as np


x= np.arange(0,math.pi*2,0.05) #arrange is used for arranging the values in the list
#print(x)

y= np.sin(x)

plt.plot(x,y)
plt.xlabel("data")
plt.ylabel("sin angle")
plt.title("Test_Sin")

plt.show()