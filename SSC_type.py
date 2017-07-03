import numpy as np
import matplotlib as mpl
from scipy import ndimage
import matplotlib.pyplot as plt
import datetime
from collections import Counter

# Call in file
f1 = '/Users/ahardin/Documents/Masters_Research/Data/Philadelphia/2008_SSC.txt'
f2 = '/Users/ahardin/Documents/Masters_Research/Data/Philadelphia/2009_SSC.txt'
f3 = '/Users/ahardin/Documents/Masters_Research/Data/Philadelphia/2010_SSC.txt'
f4 = '/Users/ahardin/Documents/Masters_Research/Data/Philadelphia/2011_SSC.txt'
f5 = '/Users/ahardin/Documents/Masters_Research/Data/Philadelphia/2012_SSC.txt'
f6 = '/Users/ahardin/Documents/Masters_Research/Data/Philadelphia/2013_SSC.txt'
f7 = '/Users/ahardin/Documents/Masters_Research/Data/Philadelphia/2006_SSC.txt'
f8 = '/Users/ahardin/Documents/Masters_Research/Data/Philadelphia/2007_SSC.txt'

data1 = np.recfromtxt(f1, unpack=True, dtype=None, names=True)
data2 = np.recfromtxt(f2, unpack=True, dtype=None, names=True)
data3 = np.recfromtxt(f3, unpack=True, dtype=None, names=True)
data4 = np.recfromtxt(f4, unpack=True, dtype=None, names=True)
data5 = np.recfromtxt(f5, unpack=True, dtype=None, names=True)
data6 = np.recfromtxt(f6, unpack=True, dtype=None, names=True)
data7 = np.recfromtxt(f7, unpack=True, dtype=None, names=True)
data8 = np.recfromtxt(f8, unpack=True, dtype=None, names=True)

ssc06 = data7['SSC']
date06 = data7['DATE']
ssc07 = data8['SSC']
date07 = data8['DATE']
ssc08 = data1['SSC']
date08 = data1['DATE']
ssc09 = data2['SSC']
date09 = data2['DATE']
ssc10 = data3['SSC']
date10 = data3['DATE']
ssc11 = data4['SSC']
date11 = data4['DATE']
ssc12 = data5['SSC']
date12 = data5['DATE']
ssc13 = data6['SSC']
date13 = data6['DATE']

# SSC type
dm, dp, dt, mm, mp, mt, t, mtt, mttt = 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 66.0, 67.0

# Number of occurrences for each air mass
#a = Counter(ssc07)
#print a
#print '---------------------------------------'

print 'PHILADELPHIA SSC DATES 2006'

# Determine dates of chosen SSC Type
print 'Dates of DM days:'
for i in range(len(ssc06)):
	if ssc06[i]==dm:
		print date06[i]
print '---------------------------------------'

print 'Dates of DP days'
for i in range(len(ssc06)):
	if ssc06[i]==dp:
		print date06[i]
print '---------------------------------------'

print 'Dates of DT days'
for i in range(len(ssc06)):
	if ssc06[i]==dt:
		print date06[i]
print '---------------------------------------'

print 'Dates of MM days'
for i in range(len(ssc06)):
	if ssc06[i]==mm:
		print date06[i]
print '---------------------------------------'

print 'Dates of MP days'
for i in range(len(ssc06)):
	if ssc06[i]==mp:
		print date06[i]
print '---------------------------------------'

print 'Dates of MT days'
for i in range(len(ssc06)):
	if ssc06[i]==mt:
		print date06[i]
print '---------------------------------------'

print 'Dates of T days'
for i in range(len(ssc06)):
	if ssc06[i]==t:
		print date06[i]
print '---------------------------------------'

print 'Dates of MT+ days'
for i in range(len(ssc06)):
	if ssc06[i]==mtt:
		print date06[i]
print '---------------------------------------'

print 'Dates of MT++ days'
for i in range(len(ssc06)):
	if ssc06[i]==mttt:
		print date06[i]
print '---------------------------------------'

	
		
		
		
		
		
		
		
		
		