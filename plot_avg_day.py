import numpy as np
import matplotlib as mpl
from scipy import ndimage
import matplotlib.pyplot as plt
import datetime as dt
from collections import Counter
from mpl_toolkits.basemap import Basemap
from scipy.interpolate import griddata

# for Boston
# took out WBZMO for DT####
## and DM WBZMO,23.006,42.365,-71.1336107 ####
## DP WBZMO,18.132,42.365,-71.1336107 ###
# DP SMMDD,17.328,42.397499,-71.1141666 ##
# MP WBZMO,19.458,42.365,-71.1336107 #
# MP WSTNW,16.134,42.338888,-71.3044444 #
# MT+ WBZMO,31.051,42.365,-71.1336107
# T WBZMO,24.418,42.365,-71.1336107 #

# for Baltimore
# on mp temps and greater than 17.5
# on T temps greater than 25
# dp temps less than 11

# New York
# for DT deleted SPNGN,40.680554,-73.7541666,5.558
# DT max temp 29.5
# for MT+ less than 19

# Philly

f1 = '/Users/ahardin/Documents/Masters_Research/Data/Boston/air_mass/mtt_temps_bos.csv'
data = np.recfromtxt(f1, unpack=True, dtype=None, names=True, delimiter=',')

#data = data[~(data['Temp'] > 25.0)]
data = data[~(data['Temp'] < 18.0)]
lon = data['Longitude']
lat = data['Latitude']
temp = data['Temp']

max_temp, min_temp = max(temp), min(temp)
print max_temp

min_lon, max_lon = min(lon), max(lon)
min_lat, max_lat = min(lat), max(lat)

# Create grid for interpolating temp
numcols, numrows = 300, 300
xi = np.linspace(min_lon, max_lon, numcols)
yi = np.linspace(min_lat, max_lat, numrows)
xi, yi = np.meshgrid(xi, yi)
zi = griddata((lon, lat), temp, (xi, yi), method='linear')

# Plot contour map
plt.figure()
CS = plt.contourf(xi, yi, zi, cmap=plt.cm.jet, levels=np.arange(10.0,30.0,.2))
#plt.colorbar()
plt.scatter(lon,lat,marker='o',c='b',s=10)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Average MT+ Day Boston')
plt.tight_layout()
plt.savefig('/Users/ahardin/Documents/Masters_Research/Data/all_cities_figures/normalized/mtt/mtt_avg_scale_bos.png')




