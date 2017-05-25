import numpy as np
import matplotlib.pylab as plt

data = np.loadtxt("/Users/huskeypm/sources/tutorials/che580/md/diffusion_a.xmgr")
dcdfreq = 1000 # dcd printed every N steps
timestep = 2e-15 # timestep [s]
stepIntoNs = dcdfreq*timestep * 1e9 # convert to ns
ts = data[:,0] * stepIntoNs  
msd = data[:,1] 
plt.plot(ts,msd)
plt.xlabel("t [ns]")
plt.ylabel("MSD [A^2]") 
plt.gcf().savefig("msd.png") 

m,b = np.polyfit(ts,msd,1) 
print "D [A^2/ns] ", m 
AngSqdpNS_UmSqdpS = 10 # A^2/ns --> um^2/s 
print "D [um^2/s] ", m * AngSqdpNS_UmSqdpS 



