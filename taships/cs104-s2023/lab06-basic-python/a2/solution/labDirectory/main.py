'''
    Olympics Medals
'''

from argparse import ArgumentParser as ap
import os

parser = ap()
parser.add_argument('--path', type=str, required = True)
args = parser.parse_args()

# dictionary for the data
totalData = {}

# looping through the directory
for fileName in os.listdir(args.path):

    # reading the file
    file = open(args.path + fileName, 'r', encoding='utf-8')
    data = file.read().split('\n')

    # loop through data of file
    for line in data:
        line = line.split('-')
        if len(line) == 4:
            country = line[0]
            totalData.setdefault(country,[0,0,0])
            totalData[country] = [totalData[country][i] + \
                int(line[i + 1]) for i in range(3)]

# sort as per gold medals and break ties lexicographically
print(dict(map(lambda x: (x, totalData[x]), sorted(
    totalData, key = lambda f: (-int(totalData[f][0]), f))
)))
