import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import sys
import shutil
import os

opt = sys.argv[1]
cc = sys.argv[2]

print(os.getcwd())

# Remove existing figure
file_path = os.path.join(os.getcwd(), 'fig', 'overview_%s_%s.png'%(cc,opt))
try:
	os.remove(file_path)
except:
	pass
                     

df1 = pd.read_csv('data/%s/%s/kmn.%s.%s.dat'%(cc, opt, opt, cc),delim_whitespace=True,header=None,
	names=['memory','Mflop/s (kmn)', 'error', 'dummy', 'permutation'])\
	.drop(['dummy','permutation', 'error'],axis=1)
df2 = pd.read_csv('data/%s/%s/knm.%s.%s.dat'%(cc, opt, opt, cc),delim_whitespace=True,header=None,
    names=['memory','Mflop/s (knm)', 'error', 'dummy', 'permutation'])\
    .drop(['dummy','permutation', 'error'],axis=1)
df3 = pd.read_csv('data/%s/%s/mnk.%s.%s.dat'%(cc, opt, opt, cc),delim_whitespace=True,header=None,
    names=['memory','Mflop/s (mnk)', 'error', 'dummy', 'permutation'])\
    .drop(['dummy','permutation', 'error'],axis=1)
df4 = pd.read_csv('data/%s/%s/mkn.%s.%s.dat'%(cc, opt, opt, cc),delim_whitespace=True,header=None,
    names=['memory','Mflop/s (mkn)', 'error', 'dummy', 'permutation'])\
    .drop(['dummy','permutation', 'error'],axis=1)
df5 = pd.read_csv('data/%s/%s/nkm.%s.%s.dat'%(cc, opt, opt, cc),delim_whitespace=True,header=None,
    names=['memory','Mflop/s (nkm)', 'error', 'dummy', 'permutation'])\
    .drop(['dummy','permutation', 'error'],axis=1)
df6 = pd.read_csv('data/%s/%s/nmk.%s.%s.dat'%(cc, opt, opt, cc),delim_whitespace=True,header=None,
    names=['memory','Mflop/s (nmk)', 'error', 'dummy', 'permutation'])\
    .drop(['dummy','permutation', 'error'],axis=1)
df7 = pd.read_csv('data/%s/%s/nat.%s.%s.dat'%(cc, opt, opt, cc),delim_whitespace=True,header=None,
    names=['memory','Mflop/s (nat)', 'error', 'dummy', 'permutation'])\
    .drop(['dummy','permutation', 'error'],axis=1)
'''
df8 = pd.read_csv('data/%s/%s/lib.%s.%s.dat'%(cc, opt, opt, cc),delim_whitespace=True,header=None,
    names=['memory','Mflop/s (lib)', 'error', 'dummy', 'permutation'])\
    .drop(['dummy','permutation', 'error'],axis=1)                                                    
'''
df9 = pd.read_csv('data/%s/%s/blk.%s.%s.dat'%(cc, opt, opt, cc),delim_whitespace=True,header=None,
    names=['memory','Mflop/s (blk)', 'error', 'dummy', 'permutation', 'block'])\
    .drop(['dummy','permutation', 'error', 'block'],axis=1)
        
		
plt.figure()
ax = df1.plot('memory',logx=False, style='.-')
df2.plot('memory', ax=ax, style='.-')
df3.plot('memory', ax=ax, style='.-')
df4.plot('memory', ax=ax, style='.-')
df5.plot('memory', ax=ax, style='.-')
df6.plot('memory', ax=ax, style='.-')
df7.plot('memory', ax=ax, style='.-')
#df8.plot('memory', ax=ax, style='.-')
df9.plot('memory', ax=ax, style='.-')
plt.legend(loc='lower left')
plt.xlabel('Memory Footprint (Kbyte)')
plt.ylabel('Performance (Mflops/s)')
plt.gca().set_ylim(bottom=0)
plt.xscale('log',basex=4)
ax = plt.gca().xaxis 
ax.set_major_formatter(ScalarFormatter()) 
plt.savefig('fig/overview_%s_%s.png'%(cc,opt), bbox_inches='tight')
plt.close()
		
