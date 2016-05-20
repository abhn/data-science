import numpy as np
# import matplotlib.pyplot as plt
from scipy import stats

values = np.random.normal(100, 20, 10000)
int_values = np.random.randint(0, 100, 50)

print np.mean(values)
print np.median(values)
print stats.mode(int_values)
print np.var(values)
print np.std(values)