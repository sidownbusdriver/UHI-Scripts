import numpy as np
import matplotlib as mpl
from scipy import ndimage
import matplotlib.pyplot as plt
import datetime as dt
from collections import Counter
import matplotlib.dates as mdates
import matplotlib.mlab as mlab
from matplotlib.ticker import MaxNLocator
import pylab

f1 = '/Users/ahardin/Documents/Masters_Research/Data/Boston/uhi_analysis/diurnal_uhi_boston.csv'
f2 = '/Users/ahardin/Documents/Masters_Research/Data/Baltimore/uhi_analysis/diurnal_uhi_baltimore.csv'
f3 = '/Users/ahardin/Documents/Masters_Research/Data/Philadelphia/uhi_analysis/diurnal_uhi_philly.csv'
f4 = '/Users/ahardin/Documents/Masters_Research/Data/New_York/uhi_analysis/diurnal_uhi_NewYork.csv'
data = np.recfromtxt(f1, unpack=True, dtype=None, names=True, delimiter=',')
data2 = np.recfromtxt(f2, unpack=True, dtype=None, names=True, delimiter=',')
data3 = np.recfromtxt(f3, unpack=True, dtype=None, names=True, delimiter=',')
data4 = np.recfromtxt(f4, unpack=True, dtype=None, names=True, delimiter=',')

# Call in data for Boston
date = data['Date']
#uhi = data['UHI']
#print len(uhi)
#uhi_cut= uhi[975:995]
#new_date = date[975:990]
string_date = [str(i) for i in date]
new_dates = [dt.datetime.strptime(t, '%Y%m%d') for t in string_date]
x_pos = np.arange(len(new_dates))
day_uhi = data['Day_UHI']
night_uhi = data['Night_UHI']
#print np.mean(night_uhi)
#uhi_cut= night_uhi[975:990]
a = len(date)
b = np.arange(0,a)

# Baltimore
day_uhi_balt = data2['Day_UHI']
night_uhi_balt = data2['Night_UHI']

# Philly
day_uhi_phil = data3['Day_UHI']
night_uhi_phil = data3['Night_UHI']

# New York City
day_uhi_ny = data4['Day_UHI']
night_uhi_ny = data4['Night_UHI']

'''
# Figure out how many times day greater than night or less than 0
great = []
for i in range(len(date)):
	if night_uhi[i] < 0.0:
		great.append(day_uhi[i])
print len(great)
'''
# Make line graph
plt.figure()
#plt.subplot(2,2,1)
#plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
#plt.xticks(x_pos, new_dates)
ax = plt.axes()
ax.xaxis.set_major_locator(MaxNLocator(7))
plt.xticks([153,306,459,612,765,918,1071], ['2007','2008','2009','2010','2011','2012','2013'])
plt.plot(b, day_uhi, linewidth=2, color='grey', label='Day')
plt.plot(b, night_uhi, linewidth=.5, color='black', label='Night')
plt.xlim(0,1224)
plt.ylim(-6,7)
plt.xlabel('Date')
plt.ylabel('UHI Intensity ($\degree$C)')
plt.title('Boston')
#fig.autofmt_xdate()
plt.gcf().autofmt_xdate()
plt.grid()
plt.tight_layout()
#plt.legend(loc='best')
plt.savefig('/Users/ahardin/Documents/Journal_Articles/JAMC/figures/diurnal_uhi_bos.pdf', dpi=300)
#plt.show()

plt.figure()
#plt.subplot(2,2,2)
ax2 = plt.axes()
ax2.xaxis.set_major_locator(MaxNLocator(7))
plt.xticks([153,306,459,612,765,918,1071], ['2007','2008','2009','2010','2011','2012','2013'])
plt.plot(b, day_uhi_balt, linewidth=2, color='grey', label='Day')
plt.plot(b, night_uhi_balt, linewidth=.5, color='black', label='Night')
plt.xlim(0,1224)
plt.ylim(-6,7)
plt.xlabel('Date')
plt.ylabel('UHI Intensity ($\degree$C)')
plt.title('Baltimore')
plt.legend(loc='best')
plt.gcf().autofmt_xdate()
plt.grid()
plt.tight_layout()
plt.savefig('/Users/ahardin/Documents/Journal_Articles/JAMC/figures/diurnal_uhi_balt.pdf', dpi=300)

plt.figure()
plt.subplot(2,2,3)
ax3 = plt.axes()
ax3.xaxis.set_major_locator(MaxNLocator(7))
plt.xticks([153,306,459,612,765,918,1071], ['2007','2008','2009','2010','2011','2012','2013'])
plt.plot(b, day_uhi_phil, linewidth=2, color='grey', label='Day')
plt.plot(b, night_uhi_phil, linewidth=.5, color='black', label='Night')
plt.xlim(0,1224)
plt.ylim(-6,7)
plt.xlabel('Date')
plt.ylabel('UHI Intensity ($\degree$C)')
plt.title('Philadelphia')
plt.gcf().autofmt_xdate()
plt.grid()
plt.tight_layout()
plt.savefig('/Users/ahardin/Documents/Journal_Articles/JAMC/figures/diurnal_uhi_phil.pdf', dpi=300)

plt.figure()
plt.subplot(2,2,4)
ax4 = plt.axes()
ax4.xaxis.set_major_locator(MaxNLocator(7))
plt.xticks([153,306,459,612,765,918,1071], ['2007','2008','2009','2010','2011','2012','2013'])
plt.plot(b, day_uhi_ny, linewidth=2, color='grey', label='Day')
plt.plot(b, night_uhi_ny, linewidth=.5, color='black', label='Night')
plt.xlim(0,1224)
plt.ylim(-6,7)
plt.xlabel('Date')
plt.ylabel('UHI Intensity ($\degree$C)')
plt.title('New York City')
plt.gcf().autofmt_xdate()
plt.grid()
plt.tight_layout()
#plt.show()
plt.savefig('/Users/ahardin/Documents/Journal_Articles/JAMC/figures/diurnal_uhi_ny.pdf', dpi=300)
'''


# Make plot of monthly UHIs
x = ['May','June','July','August','September']
bos = [1.54,1.62,1.77,2.00,2.01]
balt = [1.42,1.61,1.84,1.89,1.67]
philly = [1.67,1.82,1.96,2.12,1.95]
ny = [1.81,1.99,2.35,2.69,2.61]
x_pos = np.arange(len(x))

# Make figure
plt.figure()
plt.plot(x_pos, bos, linestyle='--', color='black', label='Boston', linewidth=2, marker='o')
plt.plot(x_pos, balt, linestyle='-.', color='black', label='Baltimore', linewidth=2, marker='o')
plt.plot(x_pos, philly, linestyle=':', color='black', label='Philadelphia', linewidth=2, marker='o')
plt.plot(x_pos, ny, label='New York', color='black', linewidth=2, marker='o')
plt.xticks(x_pos, x, rotation=0)
plt.xlabel('Month')
plt.ylabel('UHI Intensity ($\degree$C)')
plt.legend(loc='best')
plt.tight_layout()
plt.grid()
plt.savefig('/Users/ahardin/Documents/Journal_Articles/JAMC/figures/month_uhi.pdf', dpi=300)
'''









