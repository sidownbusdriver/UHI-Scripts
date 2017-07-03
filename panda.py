import pandas as pd
import numpy as np
import matplotlib as mpl
from scipy import ndimage
import matplotlib.pyplot as plt
import datetime as dt
from collections import Counter
import matplotlib.dates as mdates

# Read in the file
f1 = '/Users/ahardin/Documents/Masters_Research/Data/Boston/sort_2006_Boston.csv'
data = pd.read_csv(f1, index_col='Observation_Date')
#data = data[:900]

date = data['Observation_Date']
station = data['Station_ID']

# Convert temp to Celsius
temp = data['Outdoor_Temperature']
data['Temp_C'] = (temp-32.0)*(5.0/9.0)
temp_C = data['Temp_C']
'''
b = data.groupby(date)
temp = b['Temp_C']
max_temps =  temp.max()
min_temps = temp.min()
diff = max_temps - min_temps
print np.max(diff).index
'''
c = data.groupby(station)
temps = c['Temp_C']
print temps.std()









