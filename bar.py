# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as mpl
from scipy import ndimage
import matplotlib.pyplot as plt
import datetime as dt
from collections import Counter
import matplotlib.dates as mdates
import matplotlib.mlab as mlab

deaths = [94, 381, 3332, 187, 6660]
cause = ['Flood', 'Storm', 'Heat', 'Lightning', 'Cold']
#x_pos = np.arange(len(cause))

qstar = [529.16,470.81,290.57,527.27,439.94,410.67,405.62,376.19,527.38,510.63,331.28,430.91,519.47]
#surface = ['Backuard','Sand','Park','Asphalt','Blacktop','Tennnis Court','Concrete','Green Roof 9/02',
#'Green Roof 9/03','Green Roof 9/04','MCOM Roof 8/26','MCOM Roof 8/31','Turf']
#x_pos = np.arange(len(cause))

Rcnr = [647.9, 642.0, 480.3, 646.5, 650.7, 589.7, 626.7, 580.4, 631.0, 629.3, 534.1, 578.3, 552.0]
Rcrt = [455.2, 647.5, 405.3, 454.9, 470.5, 500.4, 0.0, 423.6, 405.8, 0.0, 0.0, 0.0, 0.0]
Rest = [614.0, 618.2, 498.6, 618.5, 611.4, 553.6, 0.0, 545.1, 596.7, 0.0, 0.0, 0.0, 0.0]
surface = ['Dry Grass','Sand','Park','Asphalt','Blacktop','Tennnis Court','Concrete','MCOM 1', 'MCOM 2', 'Artifical Turf', 'Green Roof 1',
'Green Roof 2','Green Roof 3']
x_pos = np.arange(len(surface))
w = 0.2

plt.figure()
plt.bar(x_pos, qstar, align='center', facecolor='black')
plt.xticks(x_pos, surface, rotation=90)
plt.ylabel('W/m$^2$')
plt.title('Q$^*$')
ax = plt.axes()
ax.yaxis.grid()
plt.tight_layout()
plt.autoscale(tight=True)
plt.ylim(0, 540)
plt.savefig('/Users/ahardin/Documents/Masters_Research/Thesis/figures_for_powerpoint/qstar_bar.pdf', dpi=300)
'''

plt.figure()
plt.subplot(111)
plt.bar(x_pos-w, Rcnr, width=w, align='center', facecolor='black', label='R$_{cnr}$')
plt.bar(x_pos, Rcrt, width=w, align='center', facecolor='blue', label='R$_{crt}$')
plt.bar(x_pos+w, Rest, width=w, align='center', facecolor='green', label='R$_{est}$')
plt.xticks(x_pos, surface, rotation=90)
plt.ylabel('W/m$^2$')
#plt.legend(loc='best', ncol=3)
ax = plt.axes()
ax.yaxis.grid()
plt.tight_layout()
plt.autoscale(tight=True)
plt.savefig('/Users/ahardin/Documents/Masters_Research/Thesis/figures_for_powerpoint/Rabs_bar.pdf', dpi=300)

'''


