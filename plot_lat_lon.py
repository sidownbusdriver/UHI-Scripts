import numpy as np
import matplotlib as mpl
from scipy import ndimage
import matplotlib.pyplot as plt
import datetime
from mpl_toolkits.basemap import Basemap

#### Call in the file
f1 = '/Users/ahardin/Documents/Masters_Research/Data/Philadelphia/phil_lat_lon.csv'
data = np.recfromtxt(f1, unpack=True, dtype=None, names=True, delimiter=',')

station = data['Station_ID']
lat = data['Latitude']
lon = data['Longitude']
