#!/usr/bin/python

import numpy as np

file1 = '500k_gga_cut.dat'


referenceFile = '1000k_gga_cut.dat'

refData = np.loadtxt(referenceFile)
diffData = np.loadtxt(file1)
print (refData[0,4], diffData[0,4])
realDiff = refData[:,4]-diffData[:,4]
print (realDiff[0])
imagDiff = refData[:,5]-diffData[:,5]

print (imagDiff[0])
complexRefVal = np.abs(refData[:,4])+1j*np.abs(refData[:,5])
complexDiffVal = np.abs(diffData[:,4])+np.abs(1j*diffData[:,5])
complexDiff = complexRefVal-complexDiffVal
absDiff = np.abs(complexDiff)
sumAbsDiff = np.sum(absDiff)
norm = np.sum(np.abs(complexRefVal))
print (sumAbsDiff)
R = sumAbsDiff/norm
print (R)

