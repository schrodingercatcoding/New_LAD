from scipy import linalg
from scipy.special import expit
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erf

def sigmoid_function(c, s, shift, x):
    """
    sigmoid function

    c: center of the function
    s: shape of the function
    shift: shift up by shift
    x: varible

    return f(x) + shift
    """

    return expit(s * (c -x)) + shift

def box_function(width, shift, sigma, x):
    """
    a function equals one at (shift - width/2, shift + width/2)

    sigma: how fast it goes from 1 to zero
    """
    width = width/2
    prefactor = 2.0 * 0.25
    left = erf( (1.0/width * x + 1.0/width * shift  + 1.0) / ( sigma * math.sqrt(2.0)) )
    right = erf( (1.0/width * x + 1.0/width * shift  - 1.0) / ( sigma * math.sqrt(2.0)) )

    return prefactor * (left - right)

def combined_function():

    fig, ax = plt.subplots()
    fig.set_size_inches(16,12)
    x = [ xx * 0.0005 for xx in range(-10000,10000)]

    y = [
        sigmoid_function(1.25, 100, 2.0, xx) * box_function(0.1, -1.25, 0.01, xx) +
        sigmoid_function(1.4, 100, 1.0, xx) * box_function(0.2, -1.4, 0.01, xx) +
        sigmoid_function(1.6, 100, 0.0, xx) * box_function(0.2, -1.6, 0.01, xx)
        for xx in x
    ]
    ax.scatter(x, y, label='NEW_CN', color='k', s=10)

    plt.xlim((0,2))
    plt.ylim((0,5))
    x_new_ticks = np.linspace(0,2,101)
    y_new_ticks = np.linspace(0,5,11)
    plt.xticks(x_new_ticks, fontsize=10)
    plt.yticks(y_new_ticks, fontsize=10)
    plt.xlabel('x', fontsize=10)
    plt.ylabel('y', fontsize=10)
    plt.title('box Function', fontsize=10, y=1.05)
    plt.legend(loc='best', fontsize=10)
    plt.show()

def plot_sigmoid():
    fig, ax = plt.subplots()
    fig.set_size_inches(16,12)
    x = [ xx * 0.005 for xx in range(-1000,1000)]
    y_sigmoid1 = [sigmoid_function(1.25, 50, 2.0, xx) for xx in x]
    y_sigmoid2 = [sigmoid_function(1.4, 50, 1.0, xx) for xx in x]
    y_sigmoid3 = [sigmoid_function(1.6, 50, 0.0, xx) for xx in x]
    ax.scatter(x, y_sigmoid1, label='center=%10.4f'%(1.25), color='k', s=10)
    ax.scatter(x, y_sigmoid2, label='center=%10.4f'%(1.4), color='r', s=10)
    ax.scatter(x, y_sigmoid3, label='center=%10.4f'%(1.6), color='b', s=10)
    plt.xlim((-5,5))
    plt.ylim((0,5))
    x_new_ticks = np.linspace(-5,5,11)
    y_new_ticks = np.linspace(0,5,11)
    plt.xticks(x_new_ticks, fontsize=10)
    plt.yticks(y_new_ticks, fontsize=10)
    plt.xlabel('x', fontsize=10)
    plt.ylabel('y', fontsize=10)
    plt.title('sigmoid Function', fontsize=10, y=1.05)
    plt.legend(loc='best', fontsize=10)
    plt.show()

def plot_box():
    fig, ax = plt.subplots()
    fig.set_size_inches(16,12)
    x = [ xx * 0.0005 for xx in range(-10000,10000)]
    y_box1 = [box_function(0.1, -1.25, 0.01, xx) for xx in x]
    y_box2 = [box_function(0.2, -1.4, 0.01, xx) for xx in x]
    y_box3 = [box_function(0.2, -1.6, 0.01, xx) for xx in x]
    ax.scatter(x, y_box1, label='center=%10.4f'%(1.25), color='k', s=10)
    ax.scatter(x, y_box2, label='center=%10.4f'%(1.4), color='r', s=10)
    ax.scatter(x, y_box3, label='center=%10.4f'%(1.6), color='b', s=10)
    plt.xlim((-5,5))
    plt.ylim((0,5))
    x_new_ticks = np.linspace(-5,5,101)
    y_new_ticks = np.linspace(0,5,11)
    plt.xticks(x_new_ticks, fontsize=10)
    plt.yticks(y_new_ticks, fontsize=10)
    plt.xlabel('x', fontsize=10)
    plt.ylabel('y', fontsize=10)
    plt.title('box Function', fontsize=10, y=1.05)
    plt.legend(loc='best', fontsize=10)
    plt.show()

def main():
    # for debug purpose
    # plot_sigmoid()
    # plot_box()
    combined_function()


if __name__ == "__main__":
    main()