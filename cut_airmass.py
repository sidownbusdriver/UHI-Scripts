import numpy as np
import matplotlib as mpl
from scipy import ndimage
import matplotlib.pyplot as plt
import datetime 
from collections import Counter
import matplotlib.dates as mdates

# Read in data
f1 = '/Users/ahardin/Documents/Masters_Research/Data/Boston/sort_2006_Boston.csv'
f2 = '/Users/ahardin/Documents/Masters_Research/Data/Boston/2006_SSC.txt'
data = np.recfromtxt(f1, unpack=True, dtype=None, names=True, delimiter=',')
data2 = np.recfromtxt(f2, unpack=True, dtype=None, names=True)

# Variables
date = data['Observation_Date']
temp = data['Outdoor_Temperature']
temp = (temp-32.0)*(5.0/9.0)        # Convert temperature from F to celsius
ssc = data2['SSC']
ssc_date = data2['DATE']

# SSC type
dm, dp, dt, mm, mp, mt, t, mtt, mttt = 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 66.0, 67.0
'''
dm_date = ['20060506', '20060517','20060518','20060520','20060525','20060611','20060612','20060616','20060630','20060701','20060707'
,'20060724','20060806','20060809','20060810','20060811','20060812','20060813','20060816','20060817','20060821','20060822','20060823',
'20060830','20060904','20060908','20060909','20060910','20060913','20060920','20060921','20060922','20060925','20060926','20060927'
,'20060930']
'''
# Change dates to datetime object
dates = [datetime.datetime.strptime(t, '%m/%d/%Y %I:%M:%S %p') for t in date]
compare_dates = [datetime.datetime.strftime(t, '%Y%m%d') for t in dates]

# Select dates based on air mass type
dm_date = []
for i in range(len(ssc)):
	if ssc[i]==dm:
		dm_date.append(ssc_date[i])
dm_dates = [str(t) for t in dm_date] # Convert dates to string
#print dm_dates

# Only keeps data that has same date as chosen air mass
valid_date = []
valid_temp = []
for i in range(len(compare_dates)):
	for j in range(len(dm_dates)):
		if compare_dates[i] == dm_dates[j]:
			valid_date.append(date[i])
			valid_temp.append(temp[i])
print valid_temp[:100]

bad_temps = []
for i in range(len(valid_temp)):
	if valid_temp[i] < 0:
		bad_temps.append(valid_temp[i])
print bad_temps


























