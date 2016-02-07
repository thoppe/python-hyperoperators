from hyperop import hyperop

def GrahamsNumber():
    g = 6
    for n in range(1,64+1):
        g = hyperop(g)(3,3)
    return g


# Might want to grab some coffee before running this
# print GrahamsNumber()


import numpy as np
H = hyperop(4)
e = np.exp(1.0)
X =  np.linspace(e**(-e),e**(1/e),200)
Y =  [H(x,100) for x in X]

import seaborn as sns
plt = sns.plt
text= r"$\frac{x \uparrow \uparrow \infty}{x^2} $"
plt.plot(X,Y/X**2,label=text)
plt.legend(fontsize=40)
plt.ylim(0.8,1.5)
plt.xlim(0.5, 1.6)
plt.show()
