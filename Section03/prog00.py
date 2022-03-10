import numpy as np
import matplotlib.pyplot as plt

x = np.arange(6)
print(x)
type(x)

y = x + 1

plt.plot(x, y, 'o--')
plt.show()
