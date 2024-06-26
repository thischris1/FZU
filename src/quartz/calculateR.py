#!/usr/bin/python

import numpy as np
import sys
from collections import deque 
file1 = '500k_gga_cut.dat'

if (len(sys.argv)> 2):
    referenceFile = sys.argv[1]
    file1 = sys.argv[2]

else: 
    referenceFile = '1000k_gga_cut.dat'
    if (len(sys.argv)>1):
        file1 = sys.argv[1]


# open files (only last 638 lines)
print ("Comparing file " + file1 + " to reference " + referenceFile)
with open(referenceFile,'rb') as f:
          linesRef = deque(f,638)
refData = np.genfromtxt(linesRef)
print (refData[1])

#refData = np.loadtxt(referenceFile)
with open(file1,'rb') as f:
          lines = deque(f,638)
          
diffData = np.genfromtxt(lines)
# now calculate
print (refData[0,3], diffData[0,3])
realDiff = refData[:,3]-diffData[:,3]
print (realDiff[0])
imagDiff = refData[:,4]-diffData[:,4]

print (imagDiff[0])
complexRefVal = np.abs(refData[:,3])+1j*np.abs(refData[:,4])
print (complexRefVal[0])
complexDiffVal = np.abs(diffData[:,3])+1j*np.abs(diffData[:,4])
print (complexDiffVal[0])
complexDiff = complexRefVal-complexDiffVal
absDiff = np.abs(complexDiff)
sumAbsDiff = np.sum(absDiff)
norm = np.sum(np.abs(complexRefVal))
print (sumAbsDiff)
R = sumAbsDiff/norm
print ("Calculated the difference (R-Factor) between " + referenceFile + " and " +file1 + "R value is " + str(R))
print (R)

