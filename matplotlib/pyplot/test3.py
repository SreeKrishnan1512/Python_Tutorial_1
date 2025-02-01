from matplotlib import pyplot as plt
import numpy
from matplotlib.ticker import MultipleLocator



x_axis=[1,2,3,4,5]
y_axis=[1,2,3,4,5]

fig,ax= plt.subplots()
ax.plot(x_axis,y_axis,color="red")

x_ticks= MultipleLocator(0.2)
ax.min




for i in range(0,len(x_axis)):
    x,y=x_axis[i],y_axis[i]

    plt.scatter(x,y,color="black",zorder=5) #to keep the marker
    plt.text(x + 0.1, y + 0.05, (f"{x,y}"),color="black")

plt.plot(x_axis, y_axis,color="red")

plt.title("Plot Example")
plt.xlabel("x-axis")
plt.ylabel("y-label")
plt.grid(color="blue")

plt.show()