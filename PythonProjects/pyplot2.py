import matplotlib.pyplot as plt
import numpy as np

p = np.ndarray(3)
plt.bar(p,p*p,color='r',width=0.3)
plt.bar(p+0.3,p*2,color='b',width=0.3)
plt.show()
