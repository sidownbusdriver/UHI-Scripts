import numpy as np
import matplotlib as mpl
from scipy import ndimage
import matplotlib.pyplot as plt
import datetime as dt
from collections import Counter
import matplotlib.dates as mdates
import matplotlib.mlab as mlab
from matplotlib.ticker import MaxNLocator
import pylab
from scipy.interpolate import spline

f1 = '/Users/ahardin/Documents/Masters_Research/Data/cross_sections/New_York/cross_files/mm_AB.txt'
f2 = '/Users/ahardin/Documents/Masters_Research/Data/cross_sections/New_York/cross_files/mm_CD.txt'
data = np.recfromtxt(f1, unpack=True, dtype=None, names=True)
data2 = np.recfromtxt(f2, unpack=True, dtype=None, names=True)

#for name in data.dtype.names:
	#print name
	
tempAB = data['Temp']
xAB = data['X']
a = len(tempAB)
b = np.arange(0,a)

tempCD = data2['Temp']
xCD = data2['X']
c = len(tempCD)
d = np.arange(0,c)

# Create min and max for y-axis
the_temp = np.concatenate((tempAB, tempCD))
min = np.min(the_temp) - .1
max = np.max(the_temp) + .1

# Make Cross Section
plt.figure()
ax2 = plt.axes()
ax2.xaxis.set_major_locator(MaxNLocator(2))
ax1 = plt.axes()
ax1.xaxis.set_major_locator(MaxNLocator(2))
plt.subplot(211)
plt.xticks([0,a], ['A','B'])
plt.plot(b, tempAB, linewidth=1.0)
plt.xlim(0,a)
plt.ylim(min, max)
plt.ylabel('($\degree$C)')
#plt.xlabel('Distance')

plt.subplot(212)
plt.xticks([0,c], ['C','D'])
plt.plot(d, tempCD, linewidth=1.0)
plt.xlim(0,c)
plt.ylabel('($\degree$C)')
plt.xlabel('Distance')
plt.ylim(min, max)
#plt.title('Philadelphia Cross Section')
plt.tight_layout()
plt.savefig('/Users/ahardin/Documents/Masters_Research/Data/cross_sections/New_York/cross_mm.pdf', dpi=300)



