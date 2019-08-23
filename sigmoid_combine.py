from scipy import linalg
from scipy.special import expit
import math
import matplotlib.pyplot as plt
import numpy as np

def subbtion_function(beta, sigma, mu, x):
    left = beta / (2* sigma * math.gamma(1/beta))
    sub = abs(x - mu) / sigma
    right = math.exp(-math.pow(sub, beta))

    return left * right

def sigmoid_func(c, s, x):
    """
    sigmoid function

    c: center of the function
    s: shape of the function

    return f(x)
    """

    return expit(s * (c -x))


def combined_sigmoid_function(s, x, steps):
    sum = 0
    for c in steps:
        sum += sigmoid_func(c, s, x)

    return sum

### plot function
fig, ax = plt.subplots()
fig.set_size_inches(16,12)
x = [ xx * 0.02 for xx in range(50, 100)]
# y = [ sigmoid_func(1.25, 50, xx) + 2.0 for xx in x]
# y = [ sigmoid_func(1.4, 50, xx) + 1 for xx in x]
y = [ sigmoid_func(1.7, 50, xx) for xx in x]
for xx, yy in zip(x,y):
    print(xx, yy)
ax.scatter(x, y, label='sigmoid_function', color='k', s=10)
# y = [ combined_sigmoid_function(10, xx, [1.2, 1.3, 1.5]) for xx in x]
# ax.scatter(x, y, label='combined_sigmoid_function', color='k', s=10)

plt.xlim((1,2))
plt.ylim((0,5))
x_new_ticks = np.linspace(1,2,11)
y_new_ticks = np.linspace(0,5,11)
plt.xticks(x_new_ticks, fontsize=10)
plt.yticks(y_new_ticks, fontsize=10)
plt.xlabel('x', fontsize=10)
plt.ylabel('y', fontsize=10)
plt.title('Sigmoid Function', fontsize=10, y=1.05)
plt.legend(loc='best', fontsize=10)
plt.show()
# plt.savefig('%s.png'%name)