#!/usr/bin/env python

import sys
import numpy as np

filename = sys.argv[1]

depthData = np.loadtxt(filename)

numIncreases = 0
dataLength = len(depthData)
print("Data length: " + str(dataLength))
for idx in range(dataLength - 1):
    if (depthData[idx + 1] - depthData[idx]) > 0:
        numIncreases += 1

print("Depth increased " + str(numIncreases) + " times")
