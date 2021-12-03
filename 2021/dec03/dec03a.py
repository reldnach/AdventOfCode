#!/usr/bin/env python

import sys
import numpy as np

filename = sys.argv[1]

diagData = np.loadtxt(filename, dtype=str)

numInputs = len(diagData)
numBits = len(diagData[1])
print("Number of input lines:\t" + str(numInputs))
print("Number of bits:\t\t" + str(numBits))

bitTracking = [0] * numBits
aim = 0
for idx in range(numInputs):
    for bitNum in range(numBits):
        if diagData[idx][bitNum] == '1':
            bitTracking[bitNum] += 1
        elif diagData[idx][bitNum] == '0':
            bitTracking[bitNum] -= 1
        else:
            print("Unknown bit type")

# print(bitTracking)

gammaRate = 0
epsilonRate = 0

for bitNum in range(numBits):
    gammaRate = gammaRate << 1
    epsilonRate = epsilonRate << 1
    if bitTracking[bitNum] >= 0:
        gammaRate += 1
    else:
        epsilonRate += 1

print("Gamma Rate:\t\t" + str(gammaRate))
print("Epsilon Rate:\t\t" + str(epsilonRate))
print("Power:\t\t\t" + str(gammaRate * epsilonRate))
