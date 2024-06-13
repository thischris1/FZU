#!/usr/bin/python3

import numpy as np
import sys
file1 = '500k_gga_cut.dat'

if (len(sys.argv)> 1):
    file1 = sys.argv[1]

    

referenceFile = '1000k_gga_cut.dat'

refData = np.loadtxt(referenceFile)
diffData = np.loadtxt(file1)
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

