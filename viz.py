import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import sys

opt = sys.argv[1]
print(opt)
df1 = pd.read_csv('kmn.%s.gcc.dat'%opt,delim_whitespace=True,header=None,
	names=['memory','Mflop/s (kmn)', 'error', 'dummy', 'permutation'])\
	.drop(['dummy','permutation', 'error'],axis=1)
df2 = pd.read_csv('knm.%s.gcc.dat'%opt,delim_whitespace=True,header=None,
    names=['memory','Mflop/s (knm)', 'error', 'dummy', 'permutation'])\
    .drop(['dummy','permutation', 'error'],axis=1)
df3 = pd.read_csv('mnk.%s.gcc.dat'%opt,delim_whitespace=True,header=None,
    names=['memory','Mflop/s (mnk)', 'error', 'dummy', 'permutation'])\
    .drop(['dummy','permutation', 'error'],axis=1)
df4 = pd.read_csv('mkn.%s.gcc.dat'%opt,delim_whitespace=True,header=None,
    names=['memory','Mflop/s (mkn)', 'error', 'dummy', 'permutation'])\
    .drop(['dummy','permutation', 'error'],axis=1)
df5 = pd.read_csv('nkm.%s.gcc.dat'%opt,delim_whitespace=True,header=None,
    names=['memory','Mflop/s (nkm)', 'error', 'dummy', 'permutation'])\
    .drop(['dummy','permutation', 'error'],axis=1)
df6 = pd.read_csv('nmk.%s.gcc.dat'%opt,delim_whitespace=True,header=None,
    names=['memory','Mflop/s (nmk)', 'error', 'dummy', 'permutation'])\
    .drop(['dummy','permutation', 'error'],axis=1)
df7 = pd.read_csv('nat.%s.gcc.dat'%opt,delim_whitespace=True,header=None,
    names=['memory','Mflop/s (nat)', 'error', 'dummy', 'permutation'])\
    .drop(['dummy','permutation', 'error'],axis=1)
df8 = pd.read_csv('lib.%s.gcc.dat'%opt,delim_whitespace=True,header=None,
    names=['memory','Mflop/s (lib)', 'error', 'dummy', 'permutation'])\
    .drop(['dummy','permutation', 'error'],axis=1)                                                    
		
plt.figure()
ax = df1.plot('memory',logx=False)
df2.plot('memory', ax=ax)
df3.plot('memory', ax=ax)
df4.plot('memory', ax=ax)
df5.plot('memory', ax=ax)
df6.plot('memory', ax=ax)
df7.plot('memory', ax=ax)
df8.plot('memory', ax=ax)
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.xlabel('Memory Footprint (Kbyte)')
plt.ylabel('Performance (Mflops/s)')
plt.xscale('log',basex=4)
ax = plt.gca().xaxis 
ax.set_major_formatter(ScalarFormatter()) 
plt.savefig('overview_%s.png'%opt, bbox_inches='tight')
plt.close()
		
