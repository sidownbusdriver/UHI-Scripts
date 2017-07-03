import numpy as np
import matplotlib as mpl
from scipy import ndimage
import matplotlib.pyplot as plt
import datetime as dt
from collections import Counter
import matplotlib.dates as mdates
import matplotlib.mlab as mlab
from scipy.stats import norm

f1 = '/Users/ahardin/Documents/Masters_Research/Data/Philadelphia/uhi_analysis/diurnal_uhi_philly.csv'
f2 = '/Users/ahardin/Documents/Masters_Research/Data/New_York/uhi_analysis/diurnal_uhi_NewYork.csv'
f3 = '/Users/ahardin/Documents/Masters_Research/Data/Baltimore/uhi_analysis/diurnal_uhi_baltimore.csv'
f4 = '/Users/ahardin/Documents/Masters_Research/Data/Boston/uhi_analysis/diurnal_uhi_boston.csv'
data = np.recfromtxt(f1, unpack=True, dtype=None, names=True, delimiter=',')
data2 = np.recfromtxt(f2, unpack=True, dtype=None, names=True, delimiter=',')
data3 = np.recfromtxt(f3, unpack=True, dtype=None, names=True, delimiter=',')
data4 = np.recfromtxt(f4, unpack=True, dtype=None, names=True, delimiter=',')

# Call UHI's from data
date = data4['Date']
date = np.array(date, 'string')  # convert dates to string so they can be converted to datetime object
day = data4['Day_UHI']
night = data4['Night_UHI']

# Convert dates to datetime object
dates = [dt.datetime.strptime(t, '%Y%m%d') for t in date]
month = [dt.datetime.strftime(t, '%m') for t in dates]    # can change from month to year
#print month

# Seperate UHI's by month
may = []
the = []
june = []
july = []
aug = []
sep = []
for i in range(len(date)):
	if month[i] == '05':
		may.append(night[i])
	elif month[i] == '06':
		june.append(night[i])
	elif month[i] == '07':
		july.append(night[i])
	elif month[i] == '08':
		aug.append(night[i])
		the.append(date[i])
	elif month[i] == '09':
		sep.append(night[i])
#print len(june)

mayd = []
juned = []
julyd = []
augd = []
sepd = []
for i in range(len(date)):
	if month[i] == '05':
		mayd.append(day[i])
	elif month[i] == '06':
		juned.append(day[i])
	elif month[i] == '07':
		julyd.append(day[i])
	elif month[i] == '08':
		augd.append(day[i])
	elif month[i] == '09':
		sepd.append(day[i])

# Calculate monthly UHI's	
nmay = np.mean(may)
njune = np.mean(june)
njuly = np.mean(july)
naug = np.mean(aug)
nsep = np.mean(sep)

dmay = np.mean(mayd)
djune = np.mean(juned)
djuly = np.mean(julyd)
daug = np.mean(augd)
dsep = np.mean(sepd)

# Print out averages
print ('Night May:'), nmay
print ('Night June:'), njune
print ('Night July:'), njuly
print ('Night Aug:'), naug
print ('Night Sep:'), nsep
print ('----------------------------')
print ('Day May:'), dmay
print ('Day June:'), djune
print ('Day July:'), djuly
print ('Day Aug:'), daug
print ('Day Sep:'), dsep





