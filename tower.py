from hyperop import hyperop
from scipy.optimize import minimize

H = hyperop(4)

def fixed(x):
    print x[0], H(x[0],100)
    return H(x[0], 100) /np.sqrt(x[0])

import numpy as np
e = np.exp(1.0)
bounds = (e**(-e),e**(1/e))


X = np.linspace(bounds[0],bounds[1],1000)
Y = [fixed([x]) for x in X]

import matplotlib.pyplot as plt
import seaborn as sns
plt.plot(X,Y,lw=3,alpha=0.7)
plt.ylim(ymax=1.5)
plt.show()
print Y
exit()



#print fixed(1.2)
val = minimize(fixed, 1.21, bounds=(bounds,))

print val
