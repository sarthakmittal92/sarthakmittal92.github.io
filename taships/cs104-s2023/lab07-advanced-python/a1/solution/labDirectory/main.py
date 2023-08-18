'''
    Algorithm Analysis
'''

import numpy as np
from matplotlib import pyplot as plt

# common x values
X = np.arange(1,1000)

# first record 0.1nlog(n) and 0.01n^2
nlogn = 0.1 * X * np.log(X)
nsq = 0.01 * X * X

# file path format string
path = 'files/data{}.txt'

# iterate through data and create the plots
for i in range(9):

    # loop for plot(i)
    print(f'Generating plot {i}')
    qsp1 = []
    qsrp = []
    buso = []

    for j in range(i * 3, i * 3 + 3):

        # open the files and record data
        # data in 0, 3, 6.. is for QSP1
        # data in 1, 4, 7.. is for QSRP
        # data in 2, 5, 8.. is for BuSo
        y = []
        with open(path.format(j),'r',encoding='utf-8') as f:
            read = False
            for line in f:
                if read:
                    y.append(int(line))
                read = not read
            if j % 3 == 0:
                qsp1 = y
            elif j % 3 == 1:
                qsrp = y
            else:
                buso = y

    # create the plot(i)
    # you can use if-elif-else conditions for the axes labels
    plt.plot(X,qsp1)
    plt.plot(X,qsrp)
    plt.plot(X,buso)
    plt.plot(X,nlogn)
    plt.plot(X,nsq)
    plt.legend(['QSP1', 'QSRP', 'BuSo', 'nlogn', 'n^2'])
    if i < 3:
        xl = 'Random Array Size'
    elif i < 6:
        xl = 'Almost-sorted Array Size'
    else:
        xl = 'Almost-sorted-reverse Array Size'
    if i % 3 == 0:
        yl = 'Runtime'
    elif i % 3 == 1:
        yl = 'Comparisons'
    else:
        yl = 'Swaps'
    plt.xlabel(xl)
    plt.ylabel(yl)

    # saving the plot
    plt.savefig(f'plots/plot{i}.png')
    plt.clf()
