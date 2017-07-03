import numpy as np
import matplotlib as mpl
from scipy import ndimage
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates

#### Call in the file
f1 = '/Users/ahardin/Documents/Masters_Research/Data/Boston/Boston_June.csv'
data = np.recfromtxt(f1, unpack=True, dtype=None, names=True, delimiter=',')
	
# Call in data from the file
station = data['Station_ID']
rh = data['Humidity']
date = data['Observation_Date']
date = date[0:73]
dates = [dt.datetime.strptime(t, '%m/%d/%y %H:%M') for t in date]
temp = data['Outdoor_Temperature']
ws = data['Wind_Speed']
ws_alces, ws_bfdhq, ws_bvsly, ws_bosma = ws[0:73], ws[146:219], ws[438:511], ws[219:292]
temp = (temp-32.0)*(5.0/9.0)
# Convert temperature to Kelvin
kelvin = temp+273.15
# Calculate stauration vapor pressure and vapor pressure
e_s = 6.11*np.exp((2.501*10**6/461.5)*((1.0/273.15)-(1.0/kelvin)))
e = (rh/100.0)*e_s

wind_dir = data['Wind_Direction']
dir_alces, dir_bfdhq, dir_bvsly, dir_bosma = wind_dir[0:73], wind_dir[146:219], wind_dir[438:511], wind_dir[219:292]
rh_alces, rh_bfdhq, rh_bvsly, rh_bosma = rh[0:73], rh[146:219], rh[438:511], rh[219:292]
e_alces, e_bfdhq, e_bvsly, e_bosma = e[0:73], e[146:219], e[438:511], e[219:292]

t_alces = temp[0:73]
t_ernkl = temp[73:146]
t_bfdhq = temp[146:219]
t_bosma = temp[219:292]
t_mncmh = temp[292:365]
t_mrbch = temp[365:438]
t_bvsly = temp[438:511]

# Calculate UHI
bfdhq_alces = t_bfdhq - t_alces
bfdhq_bvsly = t_bfdhq - t_bvsly
bfdhq_bosma = t_bfdhq - t_bosma
#print bfdhq_alces 

# Calculate difference in vapor pressure
e_bfdhq_alces = e_bfdhq - e_alces
e_bfdhq_bvsly = e_bfdhq - e_bvsly
e_bfdhq_bosma = e_bfdhq - e_bosma

# Plot temp profile for each station
plt.figure()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y %H:%M'))
#plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(dates, t_bvsly, 'g', label='Coastal')
plt.plot(dates, t_bfdhq, 'r', label='Urban')
plt.legend(loc=4)
plt.gcf().autofmt_xdate()
plt.xticks(rotation=45)
plt.axvline(dates[24], color='black')
plt.axvline(dates[48], color='black')
plt.text(dates[2], 33, 'DT', bbox={'facecolor':'red', 'alpha':.5, 'pad':8})
plt.text(dates[26], 33, 'MT++', bbox={'facecolor':'red', 'alpha':.5, 'pad':8})
plt.text(dates[50], 33, 'MT+', bbox={'facecolor':'red', 'alpha':.5, 'pad':8})
plt.title('Temperature at BVSLY (coastal) and BFDHQ (urban)')
plt.ylabel('Temperature (C)')
plt.xlabel('Date')
plt.tight_layout()
plt.savefig('/Users/ahardin/Documents/Masters_Research/Data/Boston/figures/Coastal-Urban/BVSLY_BFDHQ.png')

##### Plots UHI index ##########
plt.figure()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y %H:%M'))
#plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(dates, bfdhq_bvsly)
plt.gcf().autofmt_xdate()
plt.xticks(rotation=45)
plt.axvline(dates[24], color='black')
plt.axvline(dates[48], color='black')
plt.text(dates[2], 13.5, 'DT', bbox={'facecolor':'red', 'alpha':.5, 'pad':8})
plt.text(dates[26], 13.5, 'MT++', bbox={'facecolor':'red', 'alpha':.5, 'pad':8})
plt.text(dates[50], 13.5, 'MT+', bbox={'facecolor':'red', 'alpha':.5, 'pad':8})
plt.axhline(0,color='black')
plt.title('Difference in Temperature between BFDHQ (urban) and BVSLY (coastal)')
plt.ylabel('Temperature (C)')
plt.xlabel('Date')
plt.tight_layout()
plt.savefig('/Users/ahardin/Documents/Masters_Research/Data/Boston/figures/Coastal-Urban/BFDHQ-BVSLY.png')

# Plot Relative humidity 
plt.figure()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y %H:%M'))
#plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(dates, rh_bvsly, 'g', label='Coastal')
plt.plot(dates, rh_bfdhq, 'r',label='Urban')
plt.legend(loc=3)
plt.gcf().autofmt_xdate()
plt.xticks(rotation=45)
plt.axvline(dates[24], color='black')
plt.axvline(dates[48], color='black')
plt.text(dates[20], 94, 'DT', bbox={'facecolor':'red', 'alpha':.5, 'pad':8})
plt.text(dates[41], 94, 'MT++', bbox={'facecolor':'red', 'alpha':.5, 'pad':8})
plt.text(dates[67], 94, 'MT+', bbox={'facecolor':'red', 'alpha':.5, 'pad':8})
plt.title('Relative Humidity at BVSLY (coastal) and BFDHQ (urban)')
plt.ylabel('Relative Humidity (%)')
plt.xlabel('Date')
plt.tight_layout()
plt.savefig('/Users/ahardin/Documents/Masters_Research/Data/Boston/figures/Coastal-Urban/BVSLY_BFDHQ_RH.png')

# Plot Wind Direction 
plt.figure()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y %H:%M'))
#plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(dates, dir_bvsly, 'g', label='Coastal')
plt.plot(dates, dir_bfdhq, 'r', label='Urban')
plt.legend(loc='upper left')
plt.gcf().autofmt_xdate()
plt.xticks(rotation=45)
plt.axvline(dates[24], color='black')
plt.axvline(dates[48], color='black')
plt.text(dates[19], 325, 'DT', bbox={'facecolor':'red', 'alpha':.5, 'pad':8})
plt.text(dates[40], 325, 'MT++', bbox={'facecolor':'red', 'alpha':.5, 'pad':8})
plt.text(dates[66], 325, 'MT+', bbox={'facecolor':'red', 'alpha':.5, 'pad':8})
plt.title('Wind Direction at BVSLY (coastal) and BFDHQ (urban)')
plt.ylabel('Wind Direction (Degrees)')
plt.xlabel('Date')
plt.tight_layout()
plt.savefig('/Users/ahardin/Documents/Masters_Research/Data/Boston/figures/Coastal-Urban/BFDHQ_BVSLY_WDIR.png')

# Plot Vapor Pressure 
plt.figure()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y %H:%M'))
#plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(dates, e_bvsly, 'g', label='Coastal')
plt.plot(dates, e_bfdhq, 'r', label='Urban')
plt.legend(loc=4)
plt.gcf().autofmt_xdate()
plt.xticks(rotation=45)
plt.axvline(dates[24], color='black')
plt.axvline(dates[48], color='black')
plt.text(dates[2], 26.9, 'DT', bbox={'facecolor':'red', 'alpha':.5, 'pad':8})
plt.text(dates[26], 26.9, 'MT++', bbox={'facecolor':'red', 'alpha':.5, 'pad':8})
plt.text(dates[50], 26.9, 'MT+', bbox={'facecolor':'red', 'alpha':.5, 'pad':8})
plt.title('Vapor Pressure at BVSLY (coastal) and BFDHQ (urban)')
plt.ylabel('Vapor Pressure (mb)')
plt.xlabel('Date')
plt.tight_layout()
plt.savefig('/Users/ahardin/Documents/Masters_Research/Data/Boston/figures/Coastal-Urban/BFDHQ_BVSLY_e.png')

# Plot difference in vapor pressure
plt.figure()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y %H:%M'))
#plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(dates, e_bfdhq_bvsly)
plt.gcf().autofmt_xdate()
plt.xticks(rotation=45)
plt.axhline(0,color='black')
plt.axvline(dates[24], color='black')
plt.axvline(dates[48], color='black')
plt.text(dates[2], 2.7, 'DT', bbox={'facecolor':'red', 'alpha':.5, 'pad':8})
plt.text(dates[26], 2.7, 'MT++', bbox={'facecolor':'red', 'alpha':.5, 'pad':8})
plt.text(dates[50], 2.7, 'MT+', bbox={'facecolor':'red', 'alpha':.5, 'pad':8})
plt.title('Difference in Vapor Pressure between BFDHQ (urban) and BVSLY (coastal)')
plt.ylabel('Vapor Pressure (mb)')
plt.xlabel('Date')
plt.tight_layout()
plt.savefig('/Users/ahardin/Documents/Masters_Research/Data/Boston/figures/Coastal-Urban/BFDHQ_BVSLY_e_diff.png')

# Plot wind speed
plt.figure()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y %H:%M'))
#plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(dates, ws_bvsly, 'g', label='Coastal')
plt.plot(dates, ws_bfdhq, 'r', label='Urban')
plt.legend(loc=2)
plt.gcf().autofmt_xdate()
plt.xticks(rotation=45)
plt.axvline(dates[24], color='black')
plt.axvline(dates[48], color='black')
plt.text(dates[20], 14.7, 'DT', bbox={'facecolor':'red', 'alpha':.5, 'pad':8})
plt.text(dates[41], 14.7, 'MT++', bbox={'facecolor':'red', 'alpha':.5, 'pad':8})
plt.text(dates[67], 14.7, 'MT+', bbox={'facecolor':'red', 'alpha':.5, 'pad':8})
plt.title('Wind Speed at BVSLY (coastal) and BFDHQ (urban)')
plt.ylabel('Wind Speed (m/s)')
plt.xlabel('Date')
plt.tight_layout()
plt.savefig('/Users/ahardin/Documents/Masters_Research/Data/Boston/figures/Coastal-Urban/BFDHQ_BVSLY_WS.png')


















