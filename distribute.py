import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erf

# Plot[2*0.25*(erf((10*x+1 -1.2*10 )/(0.01*Sqrt[2])) - erf((10*x-1-1.2*10)/(0.01*Sqrt[2]))), {x, -3, 3}]

def subbtion_function(beta, sigma, mu, x):
    left = beta / (2* sigma * math.gamma(1/beta))
    sub = abs(x - mu) / sigma
    right = math.exp(-math.pow(sub, beta))

    return left * right

def error_function(a, sigma, x, prefactor=1, shift=0):
    
    return prefactor * (1.0/(4.0 * a)) * ( erf((x+a+shift)/(1.414*sigma)) - 
                                            erf((x-a+shift)/(1.414*sigma)))
    
### plot function

fig, ax = plt.subplots()
fig.set_size_inches(16,12)
x = [ xx * 0.005 for xx in range(-1000,1000)]
# y = [ subbtion_function(beta, sigma, mu, xx) for xx in x]
# y1 = [error_function(0.005, 0.05, xx, 0.125, -1.25) for xx in x]
# y2 = [error_function(0.005, 0.025, xx, 0.125*1/1.83, -1.25) for xx in x]
y3 = [error_function(0.05, 0.01, xx, 1*0.1, -1.25) for xx in x]
# y3 = [error_function(0.005, 0.13, xx, 0.25, -1.25) for xx in x]
# y4 = [error_function(0.005, 0.14, xx, 0.25, -1.25) for xx in x]
# y5 = [error_function(0.005, 0.1, xx, 0.25, -1.25) for xx in x]
# y6 = [error_function(0.0025, 0.1, xx, 0.25, -1.25) for xx in x]

# ax.scatter(x, y1, label='a=%10.4f, sigma=%10.4f'%(0.005, 0.05), color='k', s=10)
# ax.scatter(x, y2, label='a=%10.4f, sigma=%10.4f'%(0.005, 0.025), color='r', s=10)
ax.scatter(x, y3, label='a=%10.4f, sigma=%10.4f'%(1, 0.1), color='b', s=10)

# ax.scatter(x, y3, label='a=%10.4f, sigma=%10.4f'%(0.005, 0.13), color='b', s=10)
# ax.scatter(x, y4, label='a=%10.4f, sigma=%10.4f'%(0.005, 0.14), color='m', s=10)
# ax.scatter(x, y5, label='a=%10.4f, sigma=%10.4f'%(0.005, 0.1), color='c', s=10)
# ax.scatter(x, y6, label='a=%10.4f, sigma=%10.4f'%(0.0025, 0.1), color='y', s=10)

plt.xlim((-5,5))
plt.ylim((0,2))
x_new_ticks = np.linspace(-5,5,50)
y_new_ticks = np.linspace(0,2,20)
plt.xticks(x_new_ticks, fontsize=10)
plt.yticks(y_new_ticks, fontsize=10)
plt.xlabel('x', fontsize=10)
plt.ylabel('y', fontsize=10)
plt.title('Error Function', fontsize=10, y=1.05)
plt.legend(loc='best', fontsize=10)
plt.show()
# plt.savefig('%s.png'%name)