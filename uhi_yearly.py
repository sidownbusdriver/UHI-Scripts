import numpy as np
import matplotlib as mpl
from scipy import ndimage
import matplotlib.pyplot as plt
import datetime as dt
from collections import Counter
import matplotlib.dates as mdates
import matplotlib.mlab as mlab
from scipy.stats import norm

f1 = '/Users/ahardin/Documents/Masters_Research/Data/Philadelphia/uhi_analysis/diurnal_uhi_philly.csv'
f2 = '/Users/ahardin/Documents/Masters_Research/Data/New_York/uhi_analysis/diurnal_uhi_NewYork.csv'
f3 = '/Users/ahardin/Documents/Masters_Research/Data/Baltimore/uhi_analysis/diurnal_uhi_baltimore.csv'
f4 = '/Users/ahardin/Documents/Masters_Research/Data/Boston/uhi_analysis/diurnal_uhi_boston.csv'
data = np.recfromtxt(f1, unpack=True, dtype=None, names=True, delimiter=',')
data2 = np.recfromtxt(f2, unpack=True, dtype=None, names=True, delimiter=',')
data3 = np.recfromtxt(f3, unpack=True, dtype=None, names=True, delimiter=',')
data4 = np.recfromtxt(f4, unpack=True, dtype=None, names=True, delimiter=',')

# Call UHI's from data
date = data['Date']
date = np.array(date, 'string')  # convert dates to string so they can be converted to datetime object
day = data['Day_UHI']
night = data['Night_UHI']

# Convert dates to datetime object
dates = [dt.datetime.strptime(t, '%Y%m%d') for t in date]
year = [dt.datetime.strftime(t, '%Y') for t in dates]    # can change from month to year

# Separate UHI's by year
the = []
n06n = []
n07n = []
n08n = []
n09n = []
n10n = []
n11n = []
n12n = []
n13n = []
for i in range(len(date)):
	if year[i] == '2006':
		n06n.append(night[i])
		the.append(date[i])
	elif year[i] == '2007':
		n07n.append(night[i])
	elif year[i] == '2008':
		n08n.append(night[i])
	elif year[i] == '2009':
		n09n.append(night[i])
	elif year[i] == '2010':
		n10n.append(night[i])
	elif year[i] == '2011':
		n11n.append(night[i])
	elif year[i] == '2012':
		n12n.append(night[i])
	elif year[i] == '2013':
		n13n.append(night[i])
print len(n06n)

d06d = []
d07d = []
d08d = []
d09d = []
d10d = []
d11d = []
d12d = []
d13d = []
for i in range(len(date)):
	if year[i] == '2006':
		d06d.append(day[i])
	elif year[i] == '2007':
		d07d.append(day[i])
	elif year[i] == '2008':
		d08d.append(day[i])
	elif year[i] == '2009':
		d09d.append(day[i])
	elif year[i] == '2010':
		d10d.append(day[i])
	elif year[i] == '2011':
		d11d.append(day[i])
	elif year[i] == '2012':
		d12d.append(day[i])
	elif year[i] == '2013':
		d13d.append(day[i])
		
# Calculate yearly UHI's
print('Night 2006:'), np.mean(n06n)
print('Night 2007:'), np.mean(n07n)
print('Night 2008:'), np.mean(n08n)
print('Night 2009:'), np.mean(n09n)
print('Night 2010:'), np.mean(n10n)
print('Night 2011:'), np.mean(n11n)
print('Night 2012:'), np.mean(n12n)
print('Night 2013:'), np.mean(n13n)
print ('-------------------------------------------------')
print('Day 2006:'), np.mean(d06d)
print('Day 2007:'), np.mean(d07d)
print('Day 2008:'), np.mean(d08d)
print('Day 2009:'), np.mean(d09d)
print('Day 2010:'), np.mean(d10d)
print('Day 2011:'), np.mean(d11d)
print('Day 2012:'), np.mean(d12d)
print('Day 2013:'), np.mean(d13d)




