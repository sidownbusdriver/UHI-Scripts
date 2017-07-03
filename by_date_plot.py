import numpy as np
import matplotlib as mpl
from scipy import ndimage
import matplotlib.pyplot as plt
import datetime as dt
from collections import Counter
from mpl_toolkits.basemap import Basemap
from scipy.interpolate import griddata

# 8/06/2013 for NWP
#### Call in the file
f1 = '/Users/ahardin/Documents/Graduate_School/NWP/project/20130806_Boston.csv'
data = np.recfromtxt(f1, unpack=True, dtype=None, names=True, delimiter=',')
data = data[~(data['Outdoor_Temperature'] > 110.0)]
data = data[~(data['Outdoor_Temperature'] < 32.0)]

# Call in variables
lon = data['Longitude']
lat = data['Latitude']
date = data['Observation_Date']
temp = data['Outdoor_Temperature']
temp = (temp-32.0)*(5.0/9.0)        # Convert temperature from F to celsius 

# Change dates to datetime object
dates = [dt.datetime.strptime(t, '%m/%d/%Y %I:%M:%S %p') for t in date]
compare_dates = [dt.datetime.strftime(t, '%Y%m%d %I%M %p') for t in dates]
#print compare_dates

'''
# Date you want to pull out
begin_date = dt.datetime(2006,8,1,0,0,0)
end_date = dt.datetime(2006,8,2,0,0,0)

# Cut down data to just the days wanted
valid_dates = []
valid_lat = []
valid_lon = []
valid_temp = []

for i in range(len(dates)):
	if dates[i] >= begin_date and dates[i] < end_date:
		valid_dates.append(date[i])
		valid_lat.append(lat[i])
		valid_temp.append(temp[i])
for i in range(len(dates)):
	if dates[i] >= begin_date and dates[i] < end_date:
		valid_lon.append(lon[i])
'''
#print valid_dates[:34]
# Loop through desired timestep
new_dates = []
new_temp = []
new_lat = []
new_lon = []
timestep = '20130806 1100 PM'
hour = timestep[9:11]+timestep[14:16]
for i in range(len(compare_dates)):
	if compare_dates[i] == timestep:
		new_dates.append(date[i])
		new_temp.append(temp[i])
		new_lat.append(lat[i])
		new_lon.append(lon[i])
the_temp = np.around(new_temp, decimals=3)
min_temp, max_temp = min(the_temp), max(the_temp)
#print the_temp
#the_lat = np.around(new_lat, decimals=6)
#the_lon = np.around(new_lon, decimals=6)
#print the_temp
#print the_lon
#print the_lat
min_lon, max_lon = min(new_lon), max(new_lon)
min_lat, max_lat = min(new_lat), max(new_lat)
'''
# Create a basemap
m = Basemap(resolution='i', projection='lcc', llcrnrlon=-71.8,
            llcrnrlat=42.0, urcrnrlon=-70.5, urcrnrlat=42.7, lat_1=38.5, lon_0=-97.5,
            lat_2=38.5, rsphere=(6378137.00, 6356752.3142), area_thresh=10000)
            
m.drawcoastlines()    # Draws the coastlines
m.drawstates()        # Draw the state borders
m.fillcontinents(color='#DADADA', lake_color='aqua')    # Fill the continents with a color
m.drawmapboundary(fill_color='aqua')     # This will plot the oceans the given color

# Plot station location on basemap
new_lon, new_lat = m(the_lon, the_lat)
for i in range(len(new_lon)):
	x = new_lon[i]
	y = new_lat[i]
	m.plot(x, y, 'rv')
	#plt.savefig('/Users/ahardin/Documents/Masters_Research/Data/Boston/figures/8_1_06/8_1_06_1am_loc.png')
plt.show()
'''
# Create grid for interpolating temp
numcols, numrows = 300, 300
xi = np.linspace(min_lon, max_lon, numcols)
yi = np.linspace(min_lat, max_lat, numrows)
xi, yi = np.meshgrid(xi, yi)
zi = griddata((new_lon, new_lat), the_temp, (xi, yi), method='linear')

# Plot contour map
plt.figure()
CS = plt.contourf(xi, yi, zi, cmap=plt.cm.jet, levels=np.arange(min_temp,max_temp,.2))
plt.colorbar()
plt.scatter(new_lon,new_lat,marker='o',c='b',s=10)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Temperature on ' + timestep)
plt.savefig('/Users/ahardin/Documents/Graduate_School/NWP/project/urbanet/8_6_13_'+hour)







'''
# Loop through every hour of data
numcols, numrows = 100, 100
hour_lat = []
hour_lon = []
hour_temp = []
hour_date = []
for i in range(len(valid_dates)):
	if valid_dates[i-1] != valid_dates[i]:
		hour_lat = valid_lat[i]
		hour_lon = valid_lon[i]
		hour_temp = valid_temp[i]
		hour_date = valid_dates[i]
print hour_lat
'''		
		
		
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        