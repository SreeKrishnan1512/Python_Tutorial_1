from matplotlib import pyplot as plt

import numpy

a=numpy.array([1,2,3,4,5])
b=numpy.array([0,2,4,6,8])
plt.plot(a,b,marker="x",color= "red")


plt.title("Sample data")

plt.xlabel("x axis")
plt.ylabel("y axis")

plt.grid(color='green', linestyle='--', linewidth=0.5)

plt.show()