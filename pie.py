import numpy as np
import matplotlib as mpl
from scipy import ndimage
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates
from scipy import stats
import math

f1 = '/Users/ahardin/Documents/Masters_Research/Data/Boston/boston_SSC.txt'
data = np.recfromtxt(f1, unpack=True, dtype=None, names=True)

# Call in data
ssc = data['SSC']
ssc_date = data['DATE']

# SSC type
dm, dp, dt, mm, mp, mt, t, mtt, mttt = 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 66.0, 67.0

# Select dates for all air mass types
dm_date = []
for i in range(len(ssc)):
	if ssc[i]==dm:
		dm_date.append(ssc_date[i])
dml = (len(dm_date)/1209.)*100.

dp_date = []
for i in range(len(ssc)):
	if ssc[i]==dp:
		dp_date.append(ssc_date[i])
dpl = (len(dp_date)/1209.)*100.

dt_date = []
for i in range(len(ssc)):
	if ssc[i]==dt:
		dt_date.append(ssc_date[i])
dtl = (len(dt_date)/1209.)*100.

mm_date = []
for i in range(len(ssc)):
	if ssc[i]==mm:
		mm_date.append(ssc_date[i])
mml = (len(mm_date)/1209.)*100.
		
mp_date = []
for i in range(len(ssc)):
	if ssc[i]==mp:
		mp_date.append(ssc_date[i])
mpl = (len(mp_date)/1209.)*100.
		
mt_date = []
for i in range(len(ssc)):
	if ssc[i]==mt:
		mt_date.append(ssc_date[i])
mtl = (len(mt_date)/1209.)*100.
		
t_date = []
for i in range(len(ssc)):
	if ssc[i]==t:
		t_date.append(ssc_date[i])
tl = (len(t_date)/1209.)*100.
		
mtt_date = []
for i in range(len(ssc)):
	if ssc[i]==mtt or ssc[i]==mttt:
		mtt_date.append(ssc_date[i])
mttl = (len(mtt_date)/1209.)*100.

fracs_bos = [dml,dpl,dtl,mml,mpl,mtl,tl,mttl]
fracs_bos = np.around(fracs_bos, decimals=1)

fracs_ny = np.array([345.,61.,114.,215.,26.,274.,97.,82.])
fracs_ny = (fracs_ny/1214.)*100.

fracs_balt = np.array([321.,90.,103.,199.,25.,337.,66.,67.])
fracs_balt = (fracs_balt/1208.)*100.

fracs_phil = np.array([342.,45.,155.,195.,24.,290.,81.,77])
fracs_phil = (fracs_phil/1209.)*100.
labels = ['DM','DP','DT','MM','MP','MT','T','MT+']

plt.figure()
plt.subplot(2,2,1)
plt.pie(fracs_bos, labels=labels, autopct='%1.1f%%', colors=('b', 'g', 'r', 'c', 'y', 'm', 'orange', 'w'), labeldistance=1.05)
plt.title('Boston', fontsize=9)
plt.subplot(2,2,2)
plt.pie(fracs_ny, labels=labels, autopct='%1.1f%%', colors=('b', 'g', 'r', 'c', 'y', 'm', 'orange', 'w'), labeldistance=1.05)
plt.title('New York City', fontsize=9)
plt.subplot(2,2,3)
plt.pie(fracs_balt, labels=labels, autopct='%1.1f%%', colors=('b', 'g', 'r', 'c', 'y', 'm', 'orange', 'w'), labeldistance=1.05)
plt.title('Baltimore', fontsize=9)
plt.subplot(2,2,4)
plt.pie(fracs_phil, labels=labels, autopct='%1.1f%%', colors=('b', 'g', 'r', 'c', 'y', 'm', 'orange', 'w'), labeldistance=1.05)
plt.title('Philadelphia', fontsize=9)
#plt.suptitle('SSC Weather Types') 
plt.tight_layout()
plt.savefig('/Users/ahardin/Documents/Masters_Research/Data/SSC/all_pie_SSC.pdf', dpi=300)
#plt.show()
		



















