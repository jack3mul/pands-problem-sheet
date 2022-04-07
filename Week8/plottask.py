# To display a plot of f(x) = x, g(x) = x ** 2 & h(x) = x ** 3 
# plot in range [0,4] on 1 set of axes
# Author Kieran Mullany

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(0, 5))
ypoints = xpoints
gpoints = xpoints * xpoints
hpoints = xpoints * xpoints * xpoints

plt.plot(xpoints, ypoints, "g-o")
plt.plot(xpoints, gpoints, "b-o")
plt.plot(xpoints, hpoints, "r-o")
plt.xticks([0,1,2,3,4])
plt.title("Plots on [0,4]")
plt.legend(["f(x) = x", "g(x) = x ^ 2", "h(x) = x ^ 3"])
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

