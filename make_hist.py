import numpy as np
import matplotlib as mpl
from scipy import ndimage
import matplotlib.pyplot as plt
import datetime as dt
from collections import Counter
import matplotlib.dates as mdates
import matplotlib.mlab as mlab
from scipy.stats import norm
from scipy import stats

#f1 = '/Users/ahardin/Documents/Masters_Research/Data/Boston/uhi_analysis/diurnal_uhi_boston.csv'
#f2 = '/Users/ahardin/Documents/Masters_Research/Data/Baltimore/uhi_analysis/diurnal_uhi_baltimore.csv'
#f3 = '/Users/ahardin/Documents/Masters_Research/Data/Philadelphia/uhi_analysis/diurnal_uhi_philly.csv'
#f4 = '/Users/ahardin/Documents/Masters_Research/Data/New_York/uhi_analysis/diurnal_uhi_NewYork.csv'

f1 = '/Users/ahardin/Documents/Masters_Research/Data/Boston/uhi_analysis/uhi_boston.csv'
f2 = '/Users/ahardin/Documents/Masters_Research/Data/Baltimore/uhi_analysis/uhi_baltimore.csv'
f3 = '/Users/ahardin/Documents/Masters_Research/Data/Philadelphia/uhi_analysis/uhi_philly.csv'
f4 = '/Users/ahardin/Documents/Masters_Research/Data/New_York/uhi_analysis/uhi_NewYork.csv'

f5 = '/Users/ahardin/Documents/Masters_Research/Data/Boston/boston_SSC.txt'
f6 = '/Users/ahardin/Documents/Masters_Research/Data/Baltimore/baltimore_SSC.txt'
f7 = '/Users/ahardin/Documents/Masters_Research/Data/Philadelphia/philadelphia_SSC.txt'
f8 = '/Users/ahardin/Documents/Masters_Research/Data/New_York/NY_SSC.txt'

data = np.recfromtxt(f1, unpack=True, dtype=None, names=True, delimiter=',')
data2 = np.recfromtxt(f2, unpack=True, dtype=None, names=True, delimiter=',')
data3 = np.recfromtxt(f3, unpack=True, dtype=None, names=True, delimiter=',')
data4 = np.recfromtxt(f4, unpack=True, dtype=None, names=True, delimiter=',')

data5 = np.recfromtxt(f2, unpack=True, dtype=None, names=True)
data6 = np.recfromtxt(f2, unpack=True, dtype=None, names=True)
data7 = np.recfromtxt(f2, unpack=True, dtype=None, names=True)
data8 = np.recfromtxt(f2, unpack=True, dtype=None, names=True)

# Read in data for all cities
date_bos = data['Date']
uhi_bos = data['UHI']
date_balt = data2['Date']
uhi_balt = data2['UHI']
date_phil = data3['Date']
uhi_phil = data3['UHI']
date_ny = data['Date']
uhi_ny = data['UHI']
uhi = np.hstack((uhi_bos, uhi_balt, uhi_phil, uhi_ny))
print np.std(uhi)


'''
# Call in data
date = data['Date']
uhi = data['Night_UHI']
#uhi = data['Day_UHI']
#uhi = data['UHI']
#day_uhi = data['Day_UHI']
#night_uhi = data['Night_UHI']
ssc = data2['SSC']
ssc_date = data2['DATE']


all_std = np.std(uhi)
#all_min = np.min(uhi)
print('All STD:'), all_std
#print('All Min:'), all_min
print('----------------------------')

missing = []
for i in range(len(ssc)):
	if ssc[i] != 1 and ssc[i] !=2 and ssc[i] !=3 and ssc[i] !=4 and ssc[i] !=5 and ssc[i] !=6 and ssc[i] !=7 and ssc[i] !=66 and ssc[i] !=67:
		missing.append(ssc[i])
print len(missing)
'''
'''
# SSC type
dm, dp, dt, mm, mp, mt, t, mtt, mttt = 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 66.0, 67.0

# Select dates for all air mass types
dm_date = []
for i in range(len(ssc)):
	if ssc[i]==dm:
		dm_date.append(ssc_date[i])
dp_date = []
for i in range(len(ssc)):
	if ssc[i]==dp:
		dp_date.append(ssc_date[i])
dt_date = []
for i in range(len(ssc)):
	if ssc[i]==dt:
		dt_date.append(ssc_date[i])
mm_date = []
for i in range(len(ssc)):
	if ssc[i]==mm:
		mm_date.append(ssc_date[i])
mp_date = []
for i in range(len(ssc)):
	if ssc[i]==mp:
		mp_date.append(ssc_date[i])
mt_date = []
for i in range(len(ssc)):
	if ssc[i]==mt:
		mt_date.append(ssc_date[i])
t_date = []
for i in range(len(ssc)):
	if ssc[i]==t:
		t_date.append(ssc_date[i])
mtt_date = []
for i in range(len(ssc)):
	if ssc[i]==mtt or ssc[i]==mttt:
		mtt_date.append(ssc_date[i])
		
############# Select heat islands for each air mass ##############
dm_uhi = []
uhi_date = []
for i in range(len(uhi)):
	for j in range(len(dm_date)):
		if date[i] == dm_date[j]:
			dm_uhi.append(uhi[i])
dm_uhi = np.around(dm_uhi, decimals=3)
a = np.mean(dm_uhi)
dm_std = np.std(dm_uhi)
dm_min = np.min(dm_uhi)
print('DM:'), a
print('DM std:'), dm_std
#print('DM Min:'), dm_min
print('----------------------------')

dp_uhi = []
for i in range(len(uhi)):
	for j in range(len(dp_date)):
		if date[i] == dp_date[j]:
			dp_uhi.append(uhi[i])
dp_uhi = np.around(dp_uhi, decimals=3)
b = np.mean(dp_uhi)
dp_std = np.std(dp_uhi)
dp_min = np.min(dp_uhi)
print('DP:'), b
print('DP std:'), dp_std
#print('DP Min:'), dp_min
print('----------------------------')

dt_uhi = []
for i in range(len(uhi)):
	for j in range(len(dt_date)):
		if date[i] == dt_date[j]:
			dt_uhi.append(uhi[i])
dt_uhi = np.around(dt_uhi, decimals=3)
c = np.mean(dt_uhi)
dt_std = np.std(dt_uhi)
dt_min = np.min(dt_uhi)
print('DT:'), c
print('DT std:'), dt_std
#print('DT Min:'), dt_min
print('----------------------------')

mm_uhi = []
for i in range(len(uhi)):
	for j in range(len(mm_date)):
		if date[i] == mm_date[j]:
			mm_uhi.append(uhi[i])
mm_uhi = np.around(mm_uhi, decimals=3)
d = np.mean(mm_uhi)
mm_std = np.std(mm_uhi)
mm_min = np.min(mm_uhi)
print('MM:'), d
print('MM std:'), mm_std
#print('MM Min:'), mm_min
print('----------------------------')

mp_uhi = []
for i in range(len(uhi)):
	for j in range(len(mp_date)):
		if date[i] == mp_date[j]:
			mp_uhi.append(uhi[i])
mp_uhi = np.around(mp_uhi, decimals=3)
e = np.mean(mp_uhi)
mp_std = np.std(mp_uhi)
mp_min = np.min(mp_uhi)
print('MP:'), e
print('MP std:'), mp_std
#print('MP Min:'), mp_min
print('----------------------------')
			
mt_uhi = []
for i in range(len(uhi)):
	for j in range(len(mt_date)):
		if date[i] == mt_date[j]:
			mt_uhi.append(uhi[i])
mt_uhi = np.around(mt_uhi, decimals=3)
f = np.mean(mt_uhi)
mt_std = np.std(mt_uhi)
mt_min = np.min(mt_uhi)
print('MT:'), f
print('MT std:'), mt_std
#print('MT Min:'), mt_min
print('----------------------------')

t_uhi = []
for i in range(len(uhi)):
	for j in range(len(t_date)):
		if date[i] == t_date[j]:
			t_uhi.append(uhi[i])
t_uhi = np.around(t_uhi, decimals=3)
g = np.mean(t_uhi)
t_std = np.std(t_uhi)
t_min = np.min(t_uhi)
print('T:'), g
print('T std:'), t_std
#print('T Min:'), t_min
print('----------------------------')
			
mtt_uhi = []
for i in range(len(uhi)):
	for j in range(len(mtt_date)):
		if date[i] == mtt_date[j]:
			mtt_uhi.append(uhi[i])
mtt_uhi = np.around(mtt_uhi, decimals=3)
h = np.mean(mtt_uhi)
mtt_std = np.std(mtt_uhi)
mtt_min = np.min(mtt_uhi)
print('MTT:'), h
print('MT+ std:'), mtt_std
#print('MT+ Min:'), mtt_min
print('----------------------------')
'''
'''
# Statistics
the = uhi
mean = np.mean(the)
#max = np.max(mm_uhi)
skew = stats.skew(the)
kurtosis = stats.kurtosis(the)
std = np.std(the)
var = np.var(the)
print('---------------------------')
#print('Mean:'), mean
print('Skewness:'), skew
print('Kurtosis:'), kurtosis
print('STD:'), std
print('Variance:'), var
#print('Max:'), max
#print len(dm_uhi)

num_bins = 10
# Plot histograms
plt.figure()
plt.subplot(4,2,1)
#plt.suptitle('Frequency Distribution of Nighttime UHI Intensity Philadelphia 2006-2013')
hist, bins = np.histogram(mt_uhi, num_bins)
hist = (hist / 274.0)*100.0
widths = np.diff(bins)
plt.bar(bins[:-1],hist, widths)
plt.title('MT', fontsize=10)
plt.xlim(-1.,7)
plt.ylim(0,28)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.subplot(4,2,2)
hist, bins = np.histogram(dt_uhi, num_bins)
hist = (hist / 114.0)*100.0
widths = np.diff(bins)
plt.bar(bins[:-1],hist, widths)
plt.title('DT', fontsize=10)
plt.xlim(-1.,7)
plt.ylim(0,28)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.subplot(4,2,3)
hist, bins = np.histogram(mtt_uhi, num_bins)
hist = (hist / 82.0)*100.0
widths = np.diff(bins)
plt.bar(bins[:-1],hist, widths)
plt.title('MT+', fontsize=10)
#plt.xlabel('$\Delta$T$_u$$_-$$_r$ ($^o$C)', fontsize=9)
#plt.ylabel('Frequency (%)', fontsize=9)
plt.xlim(-1.,7)
plt.ylim(0,28)
plt.tick_params(axis='both', which='major', labelsize=10)


# Can comment this plotting out
plt.subplot(2,4,4)
hist, bins = np.histogram(dm_uhi, num_bins)
hist = (hist / 283.0)*100.0
widths = np.diff(bins)
plt.bar(bins[:-1],hist, widths)
plt.title('DM', fontsize=10)
plt.xlim(-1.5,4)
plt.ylim(0,40)
plt.tight_layout()
plt.tick_params(axis='both', which='major', labelsize=10)
plt.savefig('/Users/ahardin/Documents/Masters_Research/Data/Boston/uhi_analysis/histograms/hist_dt_mt_dm_freq_all.pdf', dpi=300)


plt.subplot(4,2,4)
hist, bins = np.histogram(uhi, num_bins)
hist = (hist / 1224.0)*100.0
widths = np.diff(bins)
plt.bar(bins[:-1],hist, widths)
plt.title('All Days', fontsize=10)
#plt.xlabel('$\Delta$T$_u$$_-$$_r$ ($^o$C)', fontsize=9)
#plt.ylabel('Frequency (%)', fontsize=9)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.xlim(-1.,7)
plt.ylim(0,28)
#plt.tight_layout()
#plt.savefig('/Users/ahardin/Documents/Masters_Research/Data/Boston/uhi_analysis/histograms/hist_dt_mt_freq_all.pdf', dpi=300)


#plt.figure()
plt.subplot(4,2,5)
#plt.suptitle('Freq. Distr. of UHI Intensity Boston 2006-2013')
hist, bins = np.histogram(dm_uhi, num_bins)
hist = (hist / 345.0)*100.0
widths = np.diff(bins)
plt.bar(bins[:-1],hist, widths)
plt.title('DM', fontsize=10)
plt.xlim(-1.,7)
plt.ylim(0,28)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.subplot(4,2,6)
hist, bins = np.histogram(dp_uhi, num_bins)
hist = (hist / 61.0)*100.0
widths = np.diff(bins)
plt.bar(bins[:-1],hist, widths)
plt.title('DP', fontsize=10)
plt.xlim(-1.,7)
plt.ylim(0,28)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.subplot(4,2,7)
hist, bins = np.histogram(mm_uhi, num_bins)
hist = (hist / 215.0)*100.0
widths = np.diff(bins)
plt.bar(bins[:-1],hist, widths)
plt.title('MM', fontsize=10)
plt.xlim(-1.,7)
plt.ylim(0,28)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.subplot(4,2,8)
hist, bins = np.histogram(mp_uhi, num_bins)
hist = (hist / 26.0)*100.0
widths = np.diff(bins)
plt.bar(bins[:-1],hist, widths)
plt.title('MP', fontsize=10)
plt.xlabel('$\Delta$T$_u$$_-$$_r$ ($^o$C)', fontsize=9)
plt.ylabel('Frequency (%)', fontsize=9)
plt.xlim(-1.,7)
plt.ylim(0,28)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.tight_layout()
plt.savefig('/Users/ahardin/Documents/Masters_Research/Thesis/figures/NY_hist.pdf', dpi=300)

plt.subplot(3,2,5)
hist, bins = np.histogram(t_uhi, num_bins)
hist = (hist / 81.0)*100.0
widths = np.diff(bins)
plt.bar(bins[:-1],hist, widths)
plt.title('T', fontsize=10)
plt.xlabel('$\Delta$T$_u$$_-$$_r$ ($^o$C)', fontsize=9)
plt.ylabel('Frequency (%)', fontsize=9)
plt.tick_params(axis='both', which='major', labelsize=10)
#plt.xlim(-1.0,4.0)
#plt.ylim(0,35)
plt.tight_layout()
#plt.show()
plt.savefig('/Users/ahardin/Documents/Masters_Research/Data/Philadelphia/uhi_analysis/histograms/hist_nonopressive_freq_night.png')		
'''	
		
		
		
		
		
		
		
		
		
		
		