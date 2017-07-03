import numpy as np
import matplotlib as mpl
from scipy import ndimage
import matplotlib.pyplot as plt
import datetime as dt
from collections import Counter
import matplotlib.dates as mdates
import csv

#### Call in the file
f1 = '/Users/ahardin/Documents/Masters_Research/Data/Boston/sort_2006_Boston.csv'
#f2 = '/Users/ahardin/Documents/Masters_Research/Data/Boston/uhi_analysis/diurnal_uhi_boston.csv'
data = np.recfromtxt(f1, unpack=True, dtype=None, usecols=(0,4,5,10,11), names=True, delimiter=',')
#data2 = np.genfromtxt(f2, delimiter=',')

date = data['Observation_Date']
station = data['Station_ID']
#a = Counter(station)
temp = data['Outdoor_Temperature']
ws = data['Average_Wind_Speed']
wd = data['Average_Wind_Direction']
ws = ws*.447                        # Convert wind speed to m/s
temp = (temp-32.0)*(5.0/9.0)        # Convert temperature from F to celsius

# Stations
urb_stations = ['BFD05','CHLSM','CHRCM','ALIVE','BOSMA','BSTNW','BFDHQ','BFDFA','BOSOX','BSTON','CHESA','EVRFD','HDSST','RXBRY','CMCFD',
'SMMDD','WBZTV','WBZT2']
rur_stations = ['HLSTN','DOVR1','MDTBM','ERNKL','WLPLB','EWPLE','SHRNS','WLLSL','SWEYM','CNTON','CNTN1','WSWDT','WSTWD','MLTNO','MLTNU',
'FXBRG','NTICK','HLBRK']

# Change dates to datetime object
dates = [dt.datetime.strptime(t, '%m/%d/%Y %I:%M:%S %p') for t in date]
compare_dates = [dt.datetime.strftime(t, '%Y%m%d %M') for t in dates]    # Selects only year/month/day minute
#compare_hours = [dt.datetime.strftime(t, '%I%M%p') for t in dates]      # Selects hour and minute, format hhmmAM/PM

begin_date = dt.datetime(2006, 9, 30, 7, 0)
end_date = dt.datetime(2006, 9, 30, 18, 0)
#begin_date = '20060501 06'
#end_date = '20060501 20'

# Select the day wanted
choose_date = '20060930 00'
save_date = choose_date[:8]  # date to put in data file
the_temp = []
the_date = []
the_station = []
the_ws = []
the_wd = []
for i in range(len(dates)):
	if compare_dates[i] == choose_date:   # maybe add in the 00 minute to get rid of timesteps not on the hour
		the_temp.append(temp[i])
		the_date.append(date[i])
		the_station.append(station[i])
		the_ws.append(ws[i])
		the_wd.append(wd[i])

the_dates = [dt.datetime.strptime(t, '%m/%d/%Y %I:%M:%S %p') for t in the_date]

# Select data based on day and night
day_date = []
day_temp = []
day_ws = []
day_wd = []
day_station = []

night_date = []
night_temp = []
night_ws = []
night_wd = []
night_station = []
for i in range(len(the_dates)):
    if the_dates[i] >= begin_date and the_dates[i] <= end_date:
    	day_date.append(the_date[i])
    	day_temp.append(the_temp[i])
    	day_ws.append(the_ws[i])
    	day_wd.append(the_wd[i])
    	day_station.append(the_station[i])
    else:
    	night_date.append(the_date[i])
    	night_temp.append(the_temp[i])
    	night_ws.append(ws[i])
    	night_wd.append(wd[i])
    	night_station.append(the_station[i])
#print day_date    	

day_ws_avg = np.mean(day_ws)
day_ws_avg = np.around(day_ws_avg, decimals=3)
day_wd_avg = np.mean(day_wd)
day_wd_avg = np.around(day_wd_avg, decimals=0)
night_ws_avg = np.mean(night_ws)
night_ws_avg = np.around(night_ws_avg, decimals=3)
night_wd_avg = np.mean(night_wd)
night_wd_avg = np.around(night_wd_avg, decimals=0)
print day_ws_avg
print day_wd_avg

###### Daytime UHI Calculation ##########################
# Select urban and rural stations
urb_station_day = []
urb_temp_day = []
urb_ws_day = []
urb_wd_day = []

rur_station_day = []
rur_temp_day = []
rur_ws_day = []
rur_wd_day = []
for i in range(len(day_temp)):
	for j in range(len(urb_stations)):
		if day_station[i] == urb_stations[j]:
			urb_temp_day.append(day_temp[i])
			urb_ws_day.append(day_ws[i])
			urb_wd_day.append(day_wd[i])
			urb_station_day.append(day_station[i])
urb_temp_day = np.around(urb_temp_day, decimals=3)
urb_temp_day = urb_temp_day[~(urb_temp_day < 0.0)]
urb_temp_avg_day = np.mean(urb_temp_day)  # average urban temps
urb_temp_avg_day = np.around(urb_temp_avg_day, decimals=3)

for i in range(len(day_temp)):
	for j in range(len(rur_stations)):
		if day_station[i] == rur_stations[j]:
			rur_temp_day.append(day_temp[i])
			rur_ws_day.append(day_ws[i])
			rur_wd_day.append(day_wd[i])
			rur_station_day.append(day_station[i])
rur_temp_day = np.around(rur_temp_day, decimals=3)
rur_temp_day = rur_temp_day[~(rur_temp_day < 0.0)]
rur_temp_avg_day = np.mean(rur_temp_day)
rur_temp_avg_day = np.around(rur_temp_avg_day, decimals=3)

# Find UHI
uhi_day = urb_temp_avg_day - rur_temp_avg_day
print uhi_day

###### Nighttime UHI Calculation ##########################
# Select urban and rural stations
urb_station_night = []
urb_temp_night = []
urb_ws_night = []
urb_wd_night = []

rur_station_night = []
rur_temp_night = []
rur_ws_night = []
rur_wd_night = []
for i in range(len(night_temp)):
	for j in range(len(urb_stations)):
		if night_station[i] == urb_stations[j]:
			urb_temp_night.append(night_temp[i])
			urb_ws_night.append(night_ws[i])
			urb_wd_night.append(night_wd[i])
			urb_station_day.append(night_station[i])
urb_temp_night = np.around(urb_temp_night, decimals=3)
urb_temp_night = urb_temp_night[~(urb_temp_night < 0.0)]
urb_temp_avg_night = np.mean(urb_temp_night)  # average urban temps
urb_temp_avg_night = np.around(urb_temp_avg_night, decimals=3)

for i in range(len(night_temp)):
	for j in range(len(rur_stations)):
		if night_station[i] == rur_stations[j]:
			rur_temp_night.append(night_temp[i])
			rur_ws_night.append(night_ws[i])
			rur_wd_night.append(night_wd[i])
			rur_station_night.append(night_station[i])
rur_temp_night = np.around(rur_temp_night, decimals=3)
rur_temp_night = rur_temp_night[~(rur_temp_night < 0.0)]
rur_temp_avg_night = np.mean(rur_temp_night)
rur_temp_avg_night = np.around(rur_temp_avg_night, decimals=3)

# Find UHI
uhi_night = urb_temp_avg_night - rur_temp_avg_night
print uhi_night
'''
# Save as csv
valid_data = np.column_stack((save_date,uhi_day,day_ws_avg,day_wd_avg,uhi_night,night_ws_avg,night_wd_avg))
the_data = np.vstack((data2,valid_data)) # use after first row has been made in file
#print the_data
np.savetxt('/Users/ahardin/Documents/Masters_Research/Data/Boston/uhi_analysis/diurnal_uhi_boston.csv', the_data, fmt='%s', delimiter=',')
'''
