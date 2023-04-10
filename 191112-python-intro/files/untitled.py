import math
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(-2*math.pi, 2*math.pi, 100)
y = math.sin(x)
plt.title(r"y = sin(x)")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot(x, y)
plt.show()

print(x)
print(y)print("你好，华科！")
print(2+3)
print("你好，华科！")
print(2+3)
