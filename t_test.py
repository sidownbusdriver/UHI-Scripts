import numpy as np
import matplotlib as mpl
from scipy import ndimage
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates
from scipy import stats

#f2 = '/Users/ahardin/Documents/Masters_Research/Data/Boston/uhi_analysis/diurnal_uhi_boston.csv'
#f2 = '/Users/ahardin/Documents/Masters_Research/Data/Baltimore/uhi_analysis/diurnal_uhi_baltimore.csv'
f2 = '/Users/ahardin/Documents/Masters_Research/Data/Philadelphia/uhi_analysis/diurnal_uhi_philly.csv'
f1 = '/Users/ahardin/Documents/Masters_Research/Data/New_York/uhi_analysis/diurnal_uhi_NewYork.csv'

#f2 = '/Users/ahardin/Documents/Masters_Research/Data/Boston/uhi_analysis/uhi_boston.csv'
#f3 = '/Users/ahardin/Documents/Masters_Research/Data/Philadelphia/uhi_analysis/uhi_philly.csv'
#f2 = '/Users/ahardin/Documents/Masters_Research/Data/New_York/uhi_analysis/uhi_NewYork.csv'

#f4 = '/Users/ahardin/Documents/Masters_Research/Data/Boston/boston_SSC.txt'
#f4 = '/Users/ahardin/Documents/Masters_Research/Data/Baltimore/baltimore_SSC.txt'
f4 = '/Users/ahardin/Documents/Masters_Research/Data/Philadelphia/philadelphia_SSC.txt'
f3 = '/Users/ahardin/Documents/Masters_Research/Data/New_York/NY_SSC.txt'
data = np.recfromtxt(f1, unpack=True, dtype=None, names=True, delimiter=',')
data1 = np.recfromtxt(f2, unpack=True, dtype=None, names=True, delimiter=',')
data2 = np.recfromtxt(f3, unpack=True, dtype=None, names=True)
data3 = np.recfromtxt(f4, unpack=True, dtype=None, names=True)

date = data['Date']
#day_uhi = data['Day_UHI']
uhi = data['Night_UHI']
#uhi = data1['UHI']
ssc = data2['SSC']
ssc_date = data2['DATE']

# other
date_oth = data1['Date']
uhi_oth = data1['Night_UHI']
ssc_oth = data3['SSC']
ssc_date_oth = data3['DATE']

# SSC type
dm, dp, dt, mm, mp, mt, t, mtt, mttt = 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 66.0, 67.0

# Other city
dt_date_oth=[]
for i in range(len(ssc_oth)):
	if ssc_oth[i]==dt:
		dt_date_oth.append(ssc_date_oth[i])
		
dt_uhi_oth=[]
for i in range(len(uhi_oth)):
	for j in range(len(dt_date_oth)):
		if date_oth[i] == dt_date_oth[j]:
			dt_uhi_oth.append(uhi_oth[i])
dt_uhi_oth = np.around(dt_uhi_oth, decimals=3)

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

dp_uhi = []
for i in range(len(uhi)):
	for j in range(len(dp_date)):
		if date[i] == dp_date[j]:
			dp_uhi.append(uhi[i])
dp_uhi = np.around(dp_uhi, decimals=3)

dt_uhi = []
for i in range(len(uhi)):
	for j in range(len(dt_date)):
		if date[i] == dt_date[j]:
			dt_uhi.append(uhi[i])
dt_uhi = np.around(dt_uhi, decimals=3)

mm_uhi = []
for i in range(len(uhi)):
	for j in range(len(mm_date)):
		if date[i] == mm_date[j]:
			mm_uhi.append(uhi[i])
mm_uhi = np.around(mm_uhi, decimals=3)

mp_uhi = []
for i in range(len(uhi)):
	for j in range(len(mp_date)):
		if date[i] == mp_date[j]:
			mp_uhi.append(uhi[i])
mp_uhi = np.around(mp_uhi, decimals=3)
			
mt_uhi = []
for i in range(len(uhi)):
	for j in range(len(mt_date)):
		if date[i] == mt_date[j]:
			mt_uhi.append(uhi[i])
mt_uhi = np.around(mt_uhi, decimals=3)

t_uhi = []
for i in range(len(uhi)):
	for j in range(len(t_date)):
		if date[i] == t_date[j]:
			t_uhi.append(uhi[i])
t_uhi = np.around(t_uhi, decimals=3)
			
mtt_uhi = []
for i in range(len(uhi)):
	for j in range(len(mtt_date)):
		if date[i] == mtt_date[j]:
			mtt_uhi.append(uhi[i])
mtt_uhi = np.around(mtt_uhi, decimals=3)
'''
# See number of negative UHIs
neg = []
the = uhi
for i in range(len(the)):
	if the[i] < 0.0:
		neg.append(the[i])
print len(neg)
'''

print np.mean(dt_uhi)
print np.mean(dt_uhi_oth)
# Calculate T-test for chosen weather types
t_test = stats.ttest_ind(dt_uhi, dt_uhi_oth)
print t_test




