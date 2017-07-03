import numpy as np
import matplotlib as mpl
from scipy import ndimage
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates
from scipy import stats
import math

f1 = '/Users/ahardin/Documents/Masters_Research/Data/Philadelphia/uhi_analysis/diurnal_uhi_philly.csv'
data = np.recfromtxt(f1, unpack=True, dtype=None, names=True, delimiter=',')

# Call in data
date = data['Date']
day_uhi = data['Day_UHI']
night_uhi = data['Night_UHI']
day_ws = data['Day_WS']
night_ws = data['Night_WS']
#print np.min(day_uhi)
'''
dayws = []
dayuhi = []
for i in range(len(day_uhi)):
	if day_uhi[i] > -2.0:
		dayws.append(day_ws[i])
		dayuhi.append(day_uhi[i])
'''
# Calculate trend line
z = np.polyfit(night_ws, night_uhi, 1)
p = np.poly1d(z)
q = np.polyfit(day_ws, day_uhi, 1)
w = np.poly1d(q)

# Plotting
plt.figure()
plt.scatter(night_ws, night_uhi)
plt.plot(night_ws, p(night_ws), color='red', linewidth=2.0)
#plt.title('Nighttime UHI and Wind Speed Boston')
plt.ylabel('UHI (C)')
plt.xlabel('Wind Speed (m/s)')
plt.tight_layout()
plt.savefig('/Users/ahardin/Documents/Masters_Research/Data/all_cities/ws/uhi_ws_Philadelphia_night.pdf', dpi=300)
#plt.show()

plt.figure()
plt.scatter(day_ws, day_uhi)
plt.plot(day_ws, w(day_ws), color='red', linewidth=2.0)
#plt.title('Daytime UHI and Wind Speed Boston')
plt.ylabel('UHI (C)')
plt.xlabel('Wind Speed (m/s)')
plt.tight_layout()
plt.savefig('/Users/ahardin/Documents/Masters_Research/Data/all_cities/ws/uhi_ws_Philadelphia_day.pdf', dpi=300)
#plt.show()


'''
day1 = []
uhi1_day = []
day2 = []
uhi2_day = []
day3 = []
uhi3_day = []
day4 = []
uhi4_day = []
for i in range(len(day_ws)):
	if day_ws[i] >= 0.0 and day_ws[i] < 1.0:
		day1.append(day_ws[i])
		uhi1_day.append(day_uhi[i])
	if day_ws[i] >= 1.0 and day_ws[i] < 2.0:
		day2.append(day_ws[i])
		uhi2_day.append(day_uhi[i])
	if day_ws[i] >= 3.0 and day_ws[i] < 4.0:
		day3.append(day_ws[i])
		uhi3_day.append(day_uhi[i])
	if day_ws[i] >= 4.0:
		day4.append(day_ws[i])
		uhi4_day.append(day_uhi[i])
#print np.mean(uhi2_day)

#plt.scatter(day_ws, day_uhi)

night1 = []
uhi1_night = []
night2 = []
uhi2_night = []
night3 = []
uhi3_night = []
night4 = []
uhi4_night = []
for i in range(len(night_ws)):
	if night_ws[i] >= 0.0 and night_ws[i] < 1.0:
		night1.append(night_ws[i])
		uhi1_night.append(night_uhi[i])
	if day_ws[i] >= 1.0 and day_ws[i] < 2.0:
		night2.append(night_ws[i])
		uhi2_night.append(night_uhi[i])
	if night_ws[i] >= 3.0 and night_ws[i] < 4.0:
		night3.append(night_ws[i])
		uhi3_night.append(night_uhi[i])
	if night_ws[i] >= 4.0:
		night4.append(night_ws[i])
		day4_night.append(night_uhi[i])
print np.mean(uhi2_night)

plt.scatter(night_uhi, night_ws)
#plt.xlim(0,6)
plt.show()
'''









