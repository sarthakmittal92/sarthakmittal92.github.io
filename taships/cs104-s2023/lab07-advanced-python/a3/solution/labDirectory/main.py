'''
    Distributions
'''

import numpy as np
from matplotlib import pyplot as plt

samples = np.random.beta(4,20,10000) * 100
plt.subplot(3,2,1)
plt.hist(samples,range(-5,50,1))

samples = np.random.exponential(0.1,10000) * 100
plt.subplot(3,2,2)
plt.hist(samples,range(-1,50,1))

samples = np.random.gamma(2,0.1,10000) * 100
plt.subplot(3,2,3)
plt.hist(samples,range(-1,50,1))

samples = np.random.laplace(0,0.5,10000) * 100
plt.subplot(3,2,4)
plt.hist(samples,range(-1,50,1))

samples = np.random.normal(0,3,10000)
plt.subplot(3,2,5)
plt.hist(samples,range(-10,11,1))

samples = np.random.poisson(3,10000)
plt.subplot(3,2,6)
plt.hist(samples,range(-1,11,1))

plt.savefig('plot.png')
