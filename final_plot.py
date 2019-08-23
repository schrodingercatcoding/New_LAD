from scipy import linalg
from scipy.special import expit
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erf

def sigmoid_func(c, s, x):
    """
    sigmoid function

    c: center of the function
    s: shape of the function

    return f(x)
    """

    return expit(s * (c -x))

def error_function(a, sigma, x, prefactor=1, shift=0):
    
    return prefactor * (1.0/(4.0 * a)) * ( erf((x+a+shift)/(1.414*sigma)) - 
                                            erf((x-a+shift)/(1.414*sigma)))

fig, ax = plt.subplots()
fig.set_size_inches(16,12)
x = [ xx * 0.005 for xx in range(-1000,1000)]
y1 = [error_function(0.1, 0.01, xx, 0.2, -1.25) * 
        (sigmoid_func(1.25, 50, xx) + 2.0) + 
        error_function(0.1, 0.01, xx, 0.2, -1.4) *
        (sigmoid_func(1.4, 50, xx) + 1.0) +
        error_function(0.1, 0.01, xx, 0.2, -1.7) *
        sigmoid_func(1.7, 50, xx)
        for xx in x]
# y1 = [sigmoid_func(1.25, 50, xx) + 2.0 for xx in x]
# y1 = [error_function(0.005, 0.05, xx, 0.125, -1.25) for xx in x]
ax.scatter(x, y1, label='a=%10.4f, sigma=%10.4f'%(0.005, 0.05), color='k', s=10)

plt.xlim((-5,5))
plt.ylim((0,5))
x_new_ticks = np.linspace(-5,5,11)
y_new_ticks = np.linspace(0,5,11)
plt.xticks(x_new_ticks, fontsize=10)
plt.yticks(y_new_ticks, fontsize=10)
plt.xlabel('x', fontsize=10)
plt.ylabel('y', fontsize=10)
plt.title('Error Function', fontsize=10, y=1.05)
plt.legend(loc='best', fontsize=10)
plt.show()
# plt.savefig('%s.png'%name)