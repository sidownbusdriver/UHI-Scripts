import numpy as np
import matplotlib as mpl
from scipy import ndimage
import matplotlib.pyplot as plt
import datetime

#### Call in the file
#f1 = '/Users/ahardin/Documents/Masters_Research/Data/Boston/sort_2006_Boston.csv'
#f2 = '/Users/ahardin/Documents/Masters_Research/Data/Boston/t_all_bos.csv'
f3 = '/Users/ahardin/Documents/Masters_Research/Data/Boston/uhi_analysis/diurnal_uhi_boston.csv'
data3 = np.recfromtxt(f3, unpack=True, dtype=None, names=True, delimiter=',')
#data = np.recfromtxt(f1, unpack=True, dtype=None, names=True, delimiter=',')
#data2 = np.recfromtxt(f2, unpack=True, dtype=None, names=True, delimiter=',')
#data1 = np.genfromtxt(f1)

#for name in data.dtype.names:
	#print name

date = data3['Date']
night_uhi = data3['Night_UHI']

temps = []
dates = []
for i in range(len(date)):
	if night_uhi[i] >= 4.0:
			temps.append(night_uhi[i])
			dates.append(date[i])
print temps
print dates




'''
ssc = data['SSC']
date = data['DATE']
#print ssc
b = 3
#c = 67

# Determine dates of chosen SSC Type
for i in range(len(ssc)):
	if ssc[i]==b:
		print date[i] 

station = data['Station_ID']
lat = data['Latitude']
lon = data['Longitude']
#print data[7]

for i in range(len(station)):
	if station[i-1] != station[i]:
		print station[i]




# Call in variable from .csv file
temp = data[:,5]
time = data[:,4]
time = time.astype(str)
print time[2]
time = range(12311)

# Plot temperature
plt.plot(time, temp)
plt.title('Temperature')
plt.savefig( '/Users/ahardin/Documents/Masters_Research/Data/temp.png')
'''