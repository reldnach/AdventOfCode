#!/usr/bin/env python

import sys
import numpy as np

filename = sys.argv[1]

pathData = np.loadtxt(filename, delimiter=' ', dtype=str)

print(pathData[0,1])

numMoves = len(pathData)
print("Number of moves:\t" + str(numMoves))
position = [0,0]
aim = 0
for idx in range(numMoves):
    if pathData[idx,0] == 'forward':
        position[0] += int(pathData[idx,1])
        position[1] += aim * int(pathData[idx,1])
    elif pathData[idx,0] == 'up':
        aim -= int(pathData[idx,1])
    elif pathData[idx,0] == 'down':
        aim += int(pathData[idx,1])
    else:
        print("Unknown movement type")

print("Horizontal Position:\t" + str(position[0]))
print("Depth:\t\t\t" + str(position[1]))
print("Aim:\t\t\t" + str(aim))
print("Multiply distance:\t" + str(position[0] * position[1]))
