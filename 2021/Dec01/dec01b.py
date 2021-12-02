#!/usr/bin/env python

import sys
import numpy as np

WINDOW_SIZE = 3

filename = sys.argv[1]

depthData = np.loadtxt(filename)

numIncreases = 0
dataLength = len(depthData)
print("Data length: " + str(dataLength))
for i in range(dataLength - WINDOW_SIZE):
    sum1 = 0
    sum2 = 0
    for j in range(WINDOW_SIZE):
        sum1 += depthData[i + j]
        sum2 += depthData[i + j + 1]
    if sum2 > sum1:
        numIncreases += 1

print("Depth increased " + str(numIncreases) + " times")
