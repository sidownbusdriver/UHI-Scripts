import numpy as np
import matplotlib as mpl
from scipy import ndimage
import matplotlib.pyplot as plt
import datetime as dt
from collections import Counter
from mpl_toolkits.basemap import Basemap
from scipy.interpolate import griddata

#### Call in the file
f1 = '/Users/ahardin/Documents/Masters_Research/Data/Boston/practice_latlon.csv'
f2 = '/Users/ahardin/Documents/Masters_Research/Data/Boston/latlon_8_1_06_1am.csv'
data = np.recfromtxt(f1, unpack=True, dtype=None, names=True, delimiter=',')
data1 = np.recfromtxt(f2, unpack=True, dtype=None, names=True, delimiter=',')

#for name in data.dtype.names:
	#print name

# Call in variables
lon = data1['Longitude']
lat = data1['Latitude']
#temp = data1['Outdoor_Temperature']
#temp = (temp-32.0)*(5.0/9.0)
#min_temp = temp.min
#max_temp = temp.max
#temp = np.vstack((temp))
#print np.shape(temp)

#print 'max lon:', max(lon)
#print 'min lon:', min(lon)
#print 'max lat:', max(lat)
#print 'min lat:', min(lat)
min_lon = max(lon)+.3
max_lon = min(lon)-.1
max_lat = max(lat)+.1
min_lat = min(lat)-.1
#print min_lon
#print max_lon

# Create a basemap
m = Basemap(resolution='i', projection='lcc', llcrnrlon=max_lon,
            llcrnrlat=min_lat, urcrnrlon=min_lon, urcrnrlat=max_lat, lat_1=38.5, lon_0=-97.5,
            lat_2=38.5, rsphere=(6378137.00, 6356752.3142), area_thresh=10000)
            
m.drawcoastlines()    # Draws the coastlines
m.drawstates()        # Draw the state borders
m.fillcontinents(color='#DADADA', lake_color='aqua')    # Fill the continents with a color
m.drawmapboundary(fill_color='aqua')     # This will plot the oceans the given color
'''
# Change lat/lon to projection space
#new_lon, new_lat = m(lon, lat)
numcols, numrows = 100, 100
#xi, yi = np.meshgrid(lon, lat)
xi = np.linspace(lon.min(), lon.max(), numcols)
yi = np.linspace(lat.min(), lat.max(), numrows)
xi, yi = np.meshgrid(xi, yi)
zi = griddata((lon, lat), temp, (xi, yi), method='linear')
#X, Y = m(xi, yi)      # change meshgrid to map projection

'''
# Plot stations
new_lon, new_lat = m(lon, lat)
for i in range(len(new_lon)):
	x = new_lon[i]
	y = new_lat[i]
	m.plot(x, y, 'rv')
plt.show()
'''
CS = plt.contourf(xi, yi, zi, cmap=plt.cm.jet)
plt.colorbar()
plt.scatter(lon,lat,marker='o',c='b',s=10)
plt.savefig('/Users/ahardin/Documents/Masters_Research/Data/Boston/figures/practice.png')
'''

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	