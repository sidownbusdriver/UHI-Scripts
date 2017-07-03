import numpy as np
import matplotlib as mpl
from scipy import ndimage
import matplotlib.pyplot as plt
import datetime as dt
from collections import Counter
import matplotlib.dates as mdates

#### Call in the file
f1 = '/Users/ahardin/Documents/Masters_Research/Data/Boston/sort_2006_Boston.csv'
data = np.recfromtxt(f1, unpack=True, dtype=None, names=True, delimiter=',')

date = data['Observation_Date']
station = data['Station_ID']
#a = Counter(station)
temp = data['Outdoor_Temperature']
temp = (temp-32.0)*(5.0/9.0)        # Convert temperature from F to celsius 
dm_date = ['20060506', '20060517','20060518','20060520','20060525','20060611','20060612','20060616','20060630','20060701','20060707'
,'20060724','20060806','20060809','20060810','20060811','20060812','20060813','20060816','20060817','20060821','20060822','20060823',
'20060830','20060904','20060908','20060909','20060910','20060913','20060920','20060921','20060922','20060925','20060926','20060927'
,'20060930']
mt_date = ['20060505', '20060718', '20060802']
hours = ['1200AM','0100AM','0200AM','0300AM','0400AM','0500AM','0600AM','0700AM','0800AM','0900AM','1000AM','1100AM','1200PM','0100PM',
'0200PM','0300PM','0400PM','0500PM','0600PM','0700PM','0800PM','0900PM','1000PM','1100PM']

# Change dates to datetime object
dates = [dt.datetime.strptime(t, '%m/%d/%Y %I:%M:%S %p') for t in date]
#compare_dates = [dt.datetime.strftime(t, '%Y%m%d') for t in dates]    # Selects only year/month/day
compare_hours = [dt.datetime.strftime(t, '%I%M%p') for t in dates]      # Selects hour and minute, format hhmmAM/PM
print compare_hours
mt_dates = [dt.datetime.strptime(t, '%Y%m%d') for t in mt_date]
mt_compare_dates = [dt.datetime.strftime(t, '%Y%m%d') for t in mt_dates]    # Selects only year/month/date
'''
# Cut down data to just the days wanted
valid_temp = []
valid_dates = []
valid_station = []
for i in range(len(dates)):
	for j in range(len(mt_date)):
		if compare_dates[i] == mt_date[j]:
			valid_temp.append(temp[i])
			valid_dates.append(date[i])
			valid_station.append(station[i])
#print max(valid_dates)

valid_temp = []
valid_dates = []
valid_station = []
# Cut down to just the urban and rural station data
for i in range(len(station)):
	if station[i] == 'WXMTH' or station[i] == 'WBZTV':
		valid_temp.append(temp[i])
		valid_dates.append(date[i])
		valid_station.append(station[i])
valid_temp = np.around(valid_temp, decimals=3)
valid_date = [dt.datetime.strptime(t, '%m/%d/%Y %I:%M:%S %p') for t in valid_dates]
compare_dates = [dt.datetime.strftime(t, '%Y%m%d %M') for t in valid_date]    # Selects only year/month/day and 00 minute

max_diff = []
diff = []
new_station = []
temper = []
new_date = []
max_temp = []
min_temp = []
day_temp = []
day_dates = []
day_station = []
for i in range(len(valid_dates)):
	if compare_dates[i] == '20060501 00':   # maybe add in the 00 minute to get rid of timesteps not on the hour
		day_temp.append(valid_temp[i])
		day_dates.append(valid_dates[i])
		day_station.append(valid_station[i])

# Select temp from each station individually
urban_temp = []
urban_stat = []
rural_temp = []
rural_stat = []
for i in range(len(day_temp)):
	if day_station[i] == 'WXMTH':
		urban_temp.append(day_temp[i])
		urban_stat.append(day_station[i])
	if day_station[i] == 'WBZTV':
		rural_temp.append(day_temp[i])
		rural_stat.append(day_station[i])
urban_temp = np.around(urban_temp, decimals=3)
rural_temp = np.around(rural_temp, decimals=3)
urb_avg = np.mean(urban_temp)
rur_avg = np.mean(rural_temp)
uhi = urb_avg - rur_avg
'''
'''
# Loop through all hourly time steps to find greatest UHI for the day selected above
temper = []
for i in range(len(valid_dates)):
	for j in range(len(hours)):
		if compare_hours[i] == hours[j]:
			temper.append(valid_temp[i])
			new_station.append(valid_station[i])
			new_date.append(valid_dates[i])
	max_temp = np.max(temper)
	min_temp = np.min(temper)
	diff = max_temp - min_temp
	print min_temp
	max_diff.append(diff)
			
#print new_date

# Find UHI at each hour step
for i in range(len(valid_dates)):
	if compare_hours[i] == '0300PM':
		temper.append(valid_temp[i])
		new_station.append(valid_station[i])
		new_date.append(valid_dates[i])
# Dont need this
		max_temp = np.max(temper)
		min_temp = np.min(temper)
		diff = max_temp-min_temp
		if valid_temp[i] == max_temp:
			max_station = new_station[i]
			the_date = new_date[i]
		if valid_temp[i] == min_temp:
			min_station = new_station[i]

max_temp = np.max(temper)
min_temp = np.min(temper)
diff = max_temp-min_temp
print diff
for i in range(len(new_date)):
	if temper[i] == max_temp:
		max_station = new_station[i]
		the_date = new_date[i]
	if temper[i] == min_temp:
		min_station = new_station[i]
print('Max station is:'), max_station
print('Min Station is:'), min_station
print('Date is:'), the_date
'''







