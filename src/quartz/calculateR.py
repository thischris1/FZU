#!/usr/bin/python3

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
with open(referenceFile,'rb') as f:
          linesRef = deque(f,638)
refData = np.genfromtxt(linesRef)


#refData = np.loadtxt(referenceFile)
with open(file1,'rb') as f:
          lines = deque(f,638)
          
diffData = np.genfromtxt(lines)
print (refData[0,4], diffData[0,4])
realDiff = refData[:,4]-diffData[:,4]
print (realDiff[0])
imagDiff = refData[:,5]-diffData[:,5]

print (imagDiff[0])
complexRefVal = np.abs(refData[:,4])+1j*np.abs(refData[:,5])
print (complexRefVal[0])
complexDiffVal = np.abs(diffData[:,4])+1j*np.abs(diffData[:,5])
print (complexDiffVal[0])
complexDiff = complexRefVal-complexDiffVal
absDiff = np.abs(complexDiff)
sumAbsDiff = np.sum(absDiff)
norm = np.sum(np.abs(complexRefVal))
print (sumAbsDiff)
R = sumAbsDiff/norm
print ("Calculated the difference (R-Factor) between " + referenceFile + " and " +file1 + "R value is " + str(R))
print (R)

