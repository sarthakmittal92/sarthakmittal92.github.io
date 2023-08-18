'''
    NumPy and The Matrix
'''

from argparse import ArgumentParser as ap
import numpy as np

def task1(matrix):
    '''print the upper diagonal matrix in column-wise fashion'''
    trans = matrix.T
    i = 1
    for row in trans:
        for elem in row[:i]:
            print(elem,end = ' ')
        print()
        i += 1

def task2(matrix):
    '''print mean, median, std (precision 2), all along x, determinant and inverse/pseudo-inverse'''
    print(np.mean(matrix,axis=0))
    print(np.median(matrix,axis=0))
    print(np.around(np.std(matrix,axis=0),decimals=2))
    D = np.linalg.det(matrix)
    if D:
        print(np.around(np.linalg.inv(matrix),decimals=2))
    else:
        print(np.around(np.linalg.pinv(matrix),decimals=2))

def task3(matrix):
    '''print after sorting along vertical and horizontal and then print flattened array'''
    print(np.sort(matrix,axis=0))
    print(np.sort(matrix,axis=1))
    print(np.sort(matrix,axis=None))

def task4(matrix):
    '''print the unique frequencies of the sorted array and the frequency of second-largest'''
    flat = np.sort(matrix,axis=None)
    _, freq = np.unique(flat,return_counts=True)
    print(flat)
    print(freq)
    print(freq[-2])

def task5(matrix, num = 0):
    '''print the padded matrix'''
    print(np.pad(matrix,((num,num),(num,num)),'constant',constant_values=((0,0),(0,0))))

if __name__ == '__main__':

    parser = ap()
    parser.add_argument('--path',type=str,required=True)
    parser.add_argument('--num',type=str,required=False)
    args = parser.parse_args()

    # converting csv to numpy
    data = np.genfromtxt(args.path,delimiter=',',dtype=int)

    # you can call the functions here
    # example call
    # task1(data)
