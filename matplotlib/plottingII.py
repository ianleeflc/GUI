## simple line and bar with errorbars
#import matplotlib.pyplot as plt
#plt.bar([1,2,3],
#             [12,13,15],
#             yerr=[3,3,3],
#             #elinewidth=1,
#             ecolor='k',
#             capsize=5,
#             #capthick=2
#             )
##
##plt.errorbar([1,2,3],
##             [12,13,15],
##             yerr=[3,3,3],
##             fmt='rs--',
##             linewidth=5,
##             elinewidth=0.5,
##             ecolor='k',
##             capsize=5,
##             capthick=5
##             )
#plt.legend(['Error bar plot'], loc='upper left')
#plt.savefig('test.png',dpi=600)
#plt.show()


## multi-bar plot
#import matplotlib.pyplot as plt
#import numpy as np
#barwidth=0.25
#
#bar1=[1,2,3,4,5]
#bar2=[4,5,6,7,8]
#bar3=[3,4,5,6,7]
#
#r1=np.arange(len(bar1))
#r2=[x+barwidth for x in r1]
#r3=[x+barwidth for x in r2]
#
#bar1_e=[1,1,1,1,1]
#bar2_e=[1,1,1,1,1]
#bar3_e=[1,1,1,1,1]
##
#plt.bar(r1,bar1,width=barwidth,yerr=bar1_e,capsize=5)
#plt.bar(r2,bar2,width=barwidth,yerr=bar2_e,capsize=5)
#plt.bar(r3,bar3,width=barwidth,yerr=bar3_e,capsize=5)
#plt.xticks([r+barwidth for r in range(len(bar1))],['A','B','C','D'])
#plt.show()
##
#import data from excel
import pandas as pd
df=pd.read_excel('data_tasks.xlsx',sheet_name='task1')
print(df)
print(df.values[:,1])
