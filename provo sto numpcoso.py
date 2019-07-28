# import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

plt.plot(t, s)

plt.title("I polli mi piacciomo")
plt.ylabel("queste sono le y")
plt.xlabel("queste sono le x")
plt.grid()

plt.savefig("test.png")
plt.show()
