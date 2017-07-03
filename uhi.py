import numpy as np
import matplotlib as mpl
from scipy import ndimage
import matplotlib.pyplot as plt
import datetime as dt
from collections import Counter
import matplotlib.dates as mdates
import csv

#### Call in the file
f1 = '/Users/ahardin/Documents/Masters_Research/Data/Boston/sort_2007_Boston.csv'
f2 = '/Users/ahardin/Documents/Masters_Research/Data/Boston/uhi_analysis/uhi_boston.csv'
data = np.recfromtxt(f1, unpack=True, dtype=None, names=True, delimiter=',')
data2 = np.genfromtxt(f2, delimiter=',')

date = data['Observation_Date']
station = data['Station_ID']
#a = Counter(station)
temp = data['Outdoor_Temperature']
temp = (temp-32.0)*(5.0/9.0)        # Convert temperature from F to celsius

# Stations
urb_stations = ['BFD05','CHLSM','CHRCM','ALIVE','BOSMA','BSTNW','BFDHQ','BFDFA','BOSOX','BSTON','CHESA','EVRFD','HDSST','RXBRY','CMCFD','SMMDD',
'WBZTV', 'WBZT2']
rur_stations = ['HLSTN', 'DOVR1', 'MDTBM', 'ERNKL', 'WLPLB', 'EWPLE', 'SHRNS', 'WLLSL', 'SWEYM', 'CNTON', 'CNTN1', 'WSWDT', 'WSTWD','MLTNO',
'MLTNU','FXBRG','NTICK','HLBRK']

# Change dates to datetime object
dates = [dt.datetime.strptime(t, '%m/%d/%Y %I:%M:%S %p') for t in date]
compare_dates = [dt.datetime.strftime(t, '%Y%m%d %M') for t in dates]    # Selects only year/month/day minute
compare_hours = [dt.datetime.strftime(t, '%I%M%p') for t in dates]      # Selects hour and minute, format hhmmAM/PM

# Select dates
the_date = '20070930 00'
day_temp = []
day_dates = []
day_station = []
for i in range(len(dates)):
	if compare_dates[i] == the_date:   # maybe add in the 00 minute to get rid of timesteps not on the hour
		day_temp.append(temp[i])
		day_dates.append(date[i])
		day_station.append(station[i])

save_date = the_date[:8]  # date to put in data file

# Select urban and rural stations
urb_station = []
urb_temp = []
rur_station = []
rur_temp = []
for i in range(len(day_temp)):
	for j in range(len(urb_stations)):
		if day_station[i] == urb_stations[j]:
			urb_temp.append(day_temp[i])
			urb_station.append(day_station[i])
#count_urb = Counter(urb_station)
#print count_urb
urb_temp = np.around(urb_temp, decimals=3)
urb_temp_avg = np.mean(urb_temp)  # average urban temps
urb_temp_avg = np.around(urb_temp_avg, decimals=3)

for i in range(len(day_temp)):
	for j in range(len(rur_stations)):
		if day_station[i] == rur_stations[j]:
			rur_temp.append(day_temp[i])
			rur_station.append(day_station[i])
#count_rur = Counter(rur_station)
#print count_rur
rur_temp = np.around(rur_temp, decimals=3)
rur_temp_avg = np.mean(rur_temp)
rur_temp_avg = np.around(rur_temp_avg, decimals=3)

# Find UHI
uhi = urb_temp_avg - rur_temp_avg

# Save as csv
valid_data = np.column_stack((save_date, uhi))
the_data = np.vstack((data2,valid_data)) # use after first row has been made in file
#print the_data
np.savetxt('/Users/ahardin/Documents/Masters_Research/Data/Boston/uhi_analysis/uhi_boston.csv', the_data, fmt='%s', delimiter=',')

'''
for i in range(len(urb_station)):
	for j in range(len(urb_stations)):
		if urb_station[i] == urb_stations[j]:
			print urb_stations[j]

'''
















