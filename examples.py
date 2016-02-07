from hyperop import hyperop

import numpy as np
e = np.exp(1.0)
X =  np.linspace(1,2,100)
Y =  [A(float(x)**0.5,100) for x in X]

import seaborn as sns
plt = sns.plt
text= r"$\frac{x \uparrow \uparrow \infty}{x} $"
plt.plot(X,Y/X,label=text)
plt.legend(fontsize=40)
plt.xlim(1,2)
plt.show()
