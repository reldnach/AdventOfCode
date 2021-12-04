#!/usr/bin/env python

import sys
import numpy as np

'''
    Return a tuple with most common bit in first postion and least common in second pos
'''
def getMostCommonBit(data, bitNum):
    bitRecord = 0
    for idx in range(len(data)):
        if data[idx][bitNum] == '1':
            bitRecord += 1
        elif data[idx][bitNum] == '0':
            bitRecord -= 1
        else:
            print("Unknown bit type")
    if (bitRecord >= 0):
        return '1','0'
    else:
        return '0','1'

'''
    Returns array of data with supplied bit value in given bit position
'''
def extractData(data, bitNum, bitVal):
    newData = []
    for idx in range(len(data)):
        if data[idx][bitNum] == bitVal:
            newData.append(data[idx])
    return newData


filename = sys.argv[1]

diagData = np.loadtxt(filename, dtype=str)

numInputs = len(diagData)
numBits = len(diagData[1])
print("Number of input lines:\t" + str(numInputs))
print("Number of bits:\t\t" + str(numBits))

oxData = diagData
co2Data = diagData
bitNum = 0
while (((len(oxData) > 1) or (len(oxData) > 1)) and (bitNum < numBits)):
# for bitNum in range(numBits, -1, -1):
    if (len(oxData) > 1):
        oxCommonBit = getMostCommonBit(oxData, bitNum)
        oxData = extractData(oxData, bitNum, oxCommonBit[0])

    if(len(co2Data) > 1):
        co2CommonBit = getMostCommonBit(co2Data, bitNum)
        co2Data = extractData(co2Data, bitNum, co2CommonBit[1])

    bitNum += 1

oxVal = int(oxData[0], 2)
co2Val = int(co2Data[0], 2)

print("Ox Val bin:\t\t" + str(oxData))
print("Ox Val dec:\t\t" + str(oxVal))
print("CO2 Val bin:\t\t" + str(co2Data))
print("CO2 Val dec:\t\t" + str(co2Val))
print("Life Support:\t\t" + str(oxVal * co2Val))
