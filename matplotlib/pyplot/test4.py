import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

x_major= np.arange(0,6,1)
y_major=np.arange(0,6,1)

fig, ax=plt.subplots()
 
ax.plot(x_major,y_major,color="red")

x_minor= MultipleLocator(0.5)
y_minor=MultipleLocator(0.5)

ax.xaxis.set_minor_locator(x_minor)
ax.yaxis.set_minor_locator(y_minor)

plt.grid(which="major",color="blue",linestyle="--")
plt.grid(which="minor",color="green",linestyle="-")

for i in range(0,len(x_major)):

    x,y= x_major[i],y_major[i]
    ax.scatter(x,y,zorder=5,color="black")
    ax.text(x+0.1,y+0.05, (f"{x,y}"),color="black")


plt.show()
