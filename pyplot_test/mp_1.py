import matplotlib.pyplot as plt
from pylab import*
import numpy as np
import sympy as sp

x = np.arange(-np.pi,np.pi,0.1)
y = np.sin(x)
plot(x,y,color = "blue",linewidth=2.0,linestyle = '-')
plt.xlim(-5,5)
plt.ylim(-1,1)
plt.xlabel("x")
plt.ylabel("y = sin(x)")
plt.title("y = sin(x)")
plt.plot(x,y)
plt.show()