import numpy as np
import matplotlib as mpl
from scipy import ndimage
import matplotlib.pyplot as plt
import datetime as dt
from collections import Counter
import matplotlib.dates as mdates
import csv

# Call in file
f1 = '/Users/ahardin/Documents/Masters_Research/Data/Philadelphia/full_Phil_lat_lon.csv'
data = np.recfromtxt(f1, unpack=True, dtype=None, names=True, delimiter=',')

station = data['Station_ID']
lat = data['Latitude']
lon = data['Longitude']
print lat[:3]

# Boston
'''stations = ['BFD05','CHLSM','CHESA','CHRCM','ALIVE','BOSMA','BSTNW','BFDHQ','BFDFA','BOSOX',
'BSTON','EVRFD','HDSST','RXBRY','CMCFD','SMMDD','WBZTV','WBZT2','HLSTN','DOVR1','MDTBM',
'ERNKL','WLPLB','EWPLE','SHRNS','WLLSL','SWEYM','CNTON','CNTN1','WSWDT','WSTWD','MLTNO',
'MLTNU','FXBRG','NTICK','HLBRK']

# Baltimore
stations = ['BLTND','BLRSM','BLTMD','BLTPC','BLMRE','BLSBR','BLMHH','LMBMS','PLDMS','TGHES',
'STFRA','BLBTW','BLTPR','BTMOR','BLTIM','BLTLK','BLTM5','BLNMS','GLNLG','DLRKS','CLKSV',
'APLMD','COLMB','CLCMB','LAUMD','CLMBA','JESUP','BRTON','MARIT','SYKES','SYKEV','EVLCT',
'LICOT','HCLMB','LAURL','LAREL']

# New York
stations = ['BRKLA','BRKL1','NYRK1','NYPSW','WWYRK','NWYR3','NWYK4','NYXHS','BROOY','BRKLN',
'NWYK1','BKLN1','LNGLN','NWYRK','BR192','BKBHS','BRKAM','IS5WC','BROKL','NYNEX','ASTOR','STAGS',
'UNNCT','BRKJT','NWYCC','BRKBD','WSTNX','BKLYN','HARIS','CDRGR','ENGWD','EMRSN','HRRSN','RYENY',
'ESTCH','HSHLW','CRSSK','NRWDN','NRWBD','RVRDG','RVRVL','BRPRS','GLRCL','WLDWC','WYCKF','FRNKM',
'WAYNN','PMNLK','PMPTN','PQNCK','LNCNP','LNCCH','LTTFA','RYMSE','MMBPC','BRNXV']'''

# Philly
stations = ['PHLD5','PHPHI','PHLDL','UPAEN','PHEXL','PHLPA','PHILA','PHLDO','TOWLS','PHLCS',
'PHMNT','PULDL','PHLD3','PHWSP','PHLDQ','FRKHS','PHLDD','PHLFF','PHLJW','PHLNE','YARDL','NWTOW',
'NWTN1','NEWTN','HLNCR','RCHBO','STHTN','WRMIN','HTBRO','HRSHM','WARMN','WRMNS','JMSNN','WRRNG',
'PHLRH','LNSDL','FRTWS','AMBLR','CLEGE','EGLVL']

the_station = []
the_lat = []
the_lon = []
for i in range(len(station)):
	for j in range(len(stations)):
		if station[i] == stations[j]:
			the_station.append(station[i])
			the_lat.append(lat[i])
			the_lon.append(lon[i])
the_station = np.array(the_station)
the_lat = np.array(the_lat)
the_lon = np.array(the_lon)
#print the_lat

print len(the_station)
print len(stations)
valid_data = np.column_stack((the_lat,the_lon))
np.savetxt('/Users/ahardin/Documents/Masters_Research/Data/Philadelphia/urb_rur_loc_phil.csv', valid_data, fmt='%s', delimiter=',')
np.savetxt('/Users/ahardin/Documents/Masters_Research/Data/Philadelphia/urb_rur_sta_phil.csv', the_station, fmt='%s', delimiter=',')
