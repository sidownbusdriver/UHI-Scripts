import numpy as np
import matplotlib as mpl
from scipy import ndimage
import matplotlib.pyplot as plt
import datetime as dt
import csv

# Call in the file
f1 = '/data/ahardin/New_York/NewYork_2007.csv'
data = np.recfromtxt(f1, unpack=True, dtype=None, names=True, delimiter=',')
#data1 = np.genfromtxt(StringIO(f1), skip_header=1, delimiter=',')

# Variables
date = data['Observation_Date']
station = data['Station_ID']
lat = data['Latitude']
lon = data['Longitude']
elev = data['Elevation']
temp = data['Outdoor_Temperature']
rh = data['Humidity']
pres = data['Pressure']
ws = data['Wind_Speed']
wd = data['Wind_Direction']
avg_ws = data['Average_Wind_Speed']
avg_wd = data['Average_Wind_Direction']
temp_rate = data['Out__Temp__Rate']
rain = data['Daily_Rainfall']
rain_rate = data['Rainfall_Rate']
in_temp = data['Indoor_Temperature']
#print date[8]

# Chamnge dates to datetime object
dates = [dt.datetime.strptime(t, '%m/%d/%Y %I:%M:%S %p') for t in date]
#print dates[8]

begin_date = dt.datetime(2007, 5, 1, 0, 0, 0)
end_date = dt.datetime(2007, 10, 1, 0, 0, 0)

#begin_date = dt.datetime.strptime('2008/5/1 12:00:00 AM', '%Y/%m/%d %I:%M:%S %p')
#end_date = dt.datetime.strptime('2008/10/1 12:00:00 AM', '%Y/%m/%d %I:%M:%S %p')

valid_date = []
valid_station = []
valid_lat = []
valid_lon = []
valid_elev = []
valid_temp = []
valid_rh = []
valid_pres = []
valid_ws = []
valid_wd = []
valid_avg_ws = []
valid_avg_wd = []
valid_temp_rate = []
valid_rain = []
valid_rain_rate = []
valid_in_temp = []
for i in range(len(dates)):
    if dates[i] >= begin_date and dates[i] <= end_date:
	valid_date.append(date[i])
    valid_station.append(station[i])
	valid_lat.append(lat[i])
	valid_lon.append(lon[i])
	valid_elev.append(elev[i])
	valid_temp.append(temp[i])
	valid_rh.append(rh[i])
	valid_pres.append(pres[i])
	valid_ws.append(ws[i])
	valid_wd.append(wd[i])
	valid_avg_ws.append(avg_ws[i])
	valid_avg_wd.append(avg_wd[i])	
	valid_temp_rate.append(temp_rate[i])
	valid_rain.append(rain[i])
	valid_rain_rate.append(rain_rate[i])
	valid_in_temp.append(in_temp[i])

#valid_date = np.vstack(valid_date)
#print np.shape(valid_rh)

# Put valid data into cloumns
valid_data = np.column_stack(( valid_station, valid_lat, valid_lon, valid_elev, valid_date, valid_temp, valid_rh, valid_pres, valid_ws, valid_wd, valid_avg_ws, valid_avg_wd, valid_temp_rate, valid_rain, valid_rain_rate, valid_in_temp))
#valid_data = np.array([valid_station, valid_lat, valid_lon, valid_elev,valid_date, valid_temp, valid_rh, valid_pres, valid_ws, valid_wd, valid_avg_ws, valid_avg_wd, valid_temp_rate, valid_rain, valid_rain_rate, valid_in_temp])
#print valid_data[0,:]
#print np.shape(valid_data)
# Save valid data as a file
head = ['Station_ID','Latitude','Longitude','Elevation','Observation_Date','Outdoor_Temperature','Humidity','Pressure','Wind_Speed','Wind_Direction','Average_Wind_Speed','Average_Wind_Direction','Out_Temp_Rate','Daily_Rainfall','Rainfall_Rate','Indoor_Temperature']
np.savetxt('/data/ahardin/New_York/cut_2007_NewYork.csv', valid_data, fmt='%s', header='Station_ID,Latitude,Longitude,Elevation,Observation_Date,Outdoor_Temperature,Humidity,Pressure,Wind_Speed,Wind_Direction,Average_Wind_Speed,Average_Wind_Direction,Out_Temp_Rate,Daily_Rainfall,Rainfall_Rate,Indoor_Temperature', delimiter=',')




'''
# Delete dates outside of threshold
#data = data[~(dates.date[:] >= begin_date.date)]
#data = data[~(dates.date[:] < end_date.date)]
#print data 


# Save as a CSV file
head = ['Station_ID','Latitude','Longitude','Elevation','Observation_Date','Outdoor_Temperature','Humidity','Pressure','Wind_Speed','Wind_Direction','Average_Wind_Speed','Average_Wind_Direction','Out__Temp__Rate','Humidity_Rate','Pressure_Rate','Hourly_Gust','Daily_Rainfall','Rainfall_Rate','Auxillary_Temperature','Aux__Tmp_Rate','Indoor_Temperature','Ind__Tmp__Rate,Light','Light_Rate']
#np.savetxt('cut_2008_Boston.csv', valid_data, header=head, delimiter=',') 
with open('cut_2008_Boston.csv', 'wt') as g:
    writer = csv.writer(g)
    writer.writerow( ('Station_ID','Latitude','Longitude','Elevation','Observation_Date','Outdoor_Temperature','Humidity','Pressure','Wind_Speed','Wind_Direction','Average_Wind_Speed','Average_Wind_Direction','Out__Temp__Rate','Humidity_Rate','Pressure_Rate','Hourly_Gust','Daily_Rainfall','Rainfall_Rate','Auxillary_Temperature','Aux__Tmp_Rate','Indoor_Temperature','Ind__Tmp__Rate,Light','Light_Rate') )
    writer.writerow(a)    
'''




















