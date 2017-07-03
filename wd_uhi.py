import numpy as np
import matplotlib as mpl
from scipy import ndimage
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates
from scipy import stats
import math

f1 = '/Users/ahardin/Documents/Masters_Research/Data/New_York/uhi_analysis/diurnal_uhi_NewYork.csv'
data = np.recfromtxt(f1, unpack=True, dtype=None, names=True, delimiter=',')

# Call in data
date = data['Date']
day_uhi = data['Day_UHI']
night_uhi = data['Night_UHI']
day_wd = data['Day_WD']
night_wd = data['Night_WD']
print np.mean(night_uhi)

# Split up uhi by wind direction
wd270d = []
wd180d = []
wd180 = []
wd270 = []
for i in range(len(night_uhi)):
	if night_wd[i] >= 100.0 and night_wd[i] <=190.0:
		wd180.append(night_uhi[i])
	elif night_wd[i] >= 210.0 and night_wd[i] <=300.0:
		wd270.append(night_uhi[i]) 

for i in range(len(day_uhi)):
	if day_wd[i] >= 100.0 and day_wd[i] <=190.0:
		wd180d.append(day_uhi[i])
	elif day_wd[i] >= 210.0 and day_wd[i] <=300.0:
		wd270d.append(day_uhi[i]) 

print len(wd180)
print('Nighttime:')
print np.mean(wd180)
print np.mean(wd270)
print('Daytime:')
print np.mean(wd180d)
print np.mean(wd270d)



'''
# Calculate trend line
z = np.polyfit(night_wd, night_uhi, 1)
p = np.poly1d(z)
q = np.polyfit(day_wd, day_uhi, 1)
w = np.poly1d(q)

# Plotting
plt.figure()
plt.scatter(night_wd, night_uhi)
plt.plot(night_wd, p(night_wd), color='red', linewidth=2.0)
#plt.title('Nighttime UHI and Wind Speed Boston')
plt.ylabel('UHI (C)')
plt.xlabel('Wind Direction (degrees)')
plt.tight_layout()
plt.savefig('/Users/ahardin/Documents/Masters_Research/Data/all_cities/wd/uhi_wd_Boston_night.pdf', dpi=300)
#plt.show()

plt.figure()
plt.scatter(day_wd, day_uhi)
plt.plot(day_wd, w(day_wd), color='red', linewidth=2.0)
#plt.title('Daytime UHI and Wind Speed Boston')
plt.ylabel('UHI (C)')
plt.xlabel('Wind Direction (degrees)')
plt.tight_layout()
plt.savefig('/Users/ahardin/Documents/Masters_Research/Data/all_cities/wd/uhi_wd_Boston_day.pdf', dpi=300)
#plt.show()
'''











