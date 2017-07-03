import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import datetime as dt
from collections import Counter
import matplotlib.dates as mdates
import matplotlib.mlab as mlab
from matplotlib.ticker import MaxNLocator
import pylab
from scipy.interpolate import spline

f1 = '/Users/ahardin/Documents/Masters_Research/Data/cross_sections/Philadelphia/cross_files/dt_AB.txt'
f2 = '/Users/ahardin/Documents/Masters_Research/Data/cross_sections/Philadelphia/cross_files/mtt_AB.txt'
f3 = '/Users/ahardin/Documents/Masters_Research/Data/cross_sections/Philadelphia/cross_files/dt_CD.txt'
f4 = '/Users/ahardin/Documents/Masters_Research/Data/cross_sections/Philadelphia/cross_files/mtt_CD.txt'

data = np.recfromtxt(f1, unpack=True, dtype=None, names=True)
data2 = np.recfromtxt(f2, unpack=True, dtype=None, names=True)
data3 = np.recfromtxt(f3, unpack=True, dtype=None, names=True)
data4 = np.recfromtxt(f4, unpack=True, dtype=None, names=True)

dt_AB = data['Temp']
mtt_AB = data2['Temp']
dt_CD = data3['Temp']
mtt_CD = data4['Temp']

the_temp = np.concatenate((dt_AB, mtt_AB, dt_CD, mtt_CD))

AB_dt = len(dt_AB)
AB_mtt = len(mtt_AB)
CD_dt = len(dt_CD)
CD_mtt = len(mtt_CD)
#print AB_dt, AB_mtt, CD_dt, CD_mtt

# Get max for x-axis
max_AB = max(AB_dt, AB_mtt)
max_CD = max(CD_dt, CD_mtt)

# Get max temp for y-axis
maxT = max(the_temp)
minT = min(the_temp)

a = np.arange(0,AB_dt)
b = np.arange(0,AB_mtt)
c = np.arange(0,CD_dt)
d = np.arange(0,CD_mtt)

'''
print len(temp_dm)
print len(temp_dp)
print len(temp_dt)
print len(temp_mm)
#print len(temp_mp)
print len(temp_mt)
print len(temp_mtt)
'''

plt.figure()
ax2 = plt.axes()
ax2.xaxis.set_major_locator(MaxNLocator(2))
ax1 = plt.axes()
ax1.xaxis.set_major_locator(MaxNLocator(2))
plt.subplot(211)
plt.xticks([0,max_AB], ['A','B'])
plt.plot(a, dt_AB, linewidth=1.0, label='DT')
plt.plot(b, mtt_AB, linewidth=1.0, label='MT+')
plt.xlim(0,max_AB)
plt.legend(loc='best')
plt.ylim(minT-.1, maxT+.1)
plt.ylabel('($\degree$C)')

plt.subplot(212)
plt.xticks([0,max_CD], ['C','D'])
plt.plot(c, dt_CD, linewidth=1.0, label='DT')
plt.plot(d, mtt_CD, '-', linewidth=1.0, label='MT+')
plt.xlim(0,max_CD)
#plt.legend()
plt.ylim(minT-.1, maxT+.1)
plt.ylabel('($\degree$C)')
plt.xlabel('Distance')
plt.tight_layout()
plt.savefig('/Users/ahardin/Documents/Journal_Articles/JAMC/figures/Philly_cross.pdf', dpi=300)



