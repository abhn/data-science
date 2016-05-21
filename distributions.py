import numpy as np
import matplotlib.pyplot as plt

# uniform distribution

values = np.random.uniform(0,100.0, 1000)
plt.hist(values, 100)
plt.show()

# normal/gaussian distribution

values = np.random.normal(0, 20, 1000)
plt.hist(values, 100)
plt.show()

