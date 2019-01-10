import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import sys
import shutil
import os

print(os.getcwd())

# Remove existing figure
file_path = os.path.join(os.getcwd(), 'fig', 'overview_lib.png')
try:
	os.remove(file_path)
except:
	pass
                     

df1 = pd.read_csv('data/gcc/nopt/lib.nopt.gcc.dat',delim_whitespace=True,header=None,
    names=['memory','Mflop/s (lib)', 'error', 'dummy', 'permutation'])\
    .drop(['dummy','permutation', 'error'],axis=1)                                                    
df2 = pd.read_csv('data/gcc/Ofast/lib.Ofast.gcc.dat',delim_whitespace=True,header=None,
    names=['memory','Mflop/s (lib)', 'error', 'dummy', 'permutation'])\
    .drop(['dummy','permutation', 'error'],axis=1)
df3 = pd.read_csv('data/gcc/Ofast_loop/lib.Ofast_loop.gcc.dat',delim_whitespace=True,header=None,
    names=['memory','Mflop/s (lib)', 'error', 'dummy', 'permutation'])\
    .drop(['dummy','permutation', 'error'],axis=1)
df4 = pd.read_csv('data/suncc/nopt/lib.nopt.suncc.dat',delim_whitespace=True,header=None,
    names=['memory','Mflop/s (lib)', 'error', 'dummy', 'permutation'])\
    .drop(['dummy','permutation', 'error'],axis=1)
df5 = pd.read_csv('data/suncc/fast/lib.fast.suncc.dat',delim_whitespace=True,header=None,
    names=['memory','Mflop/s (lib)', 'error', 'dummy', 'permutation'])\
    .drop(['dummy','permutation', 'error'],axis=1)
df6 = pd.read_csv('data/suncc/fast_loop/lib.fast_loop.suncc.dat',delim_whitespace=True,header=None,
    names=['memory','Mflop/s (lib)', 'error', 'dummy', 'permutation'])\
    .drop(['dummy','permutation', 'error'],axis=1)
        
       	    
        
		
plt.figure()
ax = df1.plot('memory',logx=False)
df2.plot('memory', ax=ax)
df3.plot('memory', ax=ax)
df4.plot('memory', ax=ax)
df5.plot('memory', ax=ax)
df6.plot('memory', ax=ax)
plt.legend(loc='lower left')
plt.xlabel('Memory Footprint (Kbyte)')
plt.ylabel('Performance (Mflops/s)')
plt.gca().set_ylim(bottom=0)
plt.xscale('log',basex=4)
ax = plt.gca().xaxis 
ax.set_major_formatter(ScalarFormatter()) 
plt.savefig('fig/overview_lib.png', bbox_inches='tight')
plt.close()
		
