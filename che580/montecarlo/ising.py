#!/usr/bin/env python
import numpy as np 
import matplotlib.pylab as plt 
"""
Bare bones ising model 

Something seems a bit buggy still, so work in progress 
"""

from math import exp
from random import randrange,choice,random
from numpy import zeros

# initialize random lattice 
def init_ising_lattice(n):
    rands= np.reshape(np.random.rand(n*n),[n,n]) 
    print rands 
    lattice = np.ones([n,n],dtype=int) 
    lattice[ rands>0.5 ] = -1
    print lattice 

    return lattice

# energy between spin 0 and its neighbors
# J is a coupling constant
# H is an applied field 
#def energydiff(S0,Sn,J,H): 
#  return 2*S0*(H+J*Sn)
def energyij(S0,Sn,J,H):
  return -S0*(H+J*Sn) 

##
## Ising simulator 
##
def ising(
    n=200,   # range in x, y directions 
    nsteps=500000,
    H=0,  # need units 
    J=1,  # [kT] 
    T=1, # temp [K]
    lattice = None # optional - pass in int array of spins (unitless) 
    ):
    nsteps = np.int(nsteps) 

    if lattice is None: 
      print "Initializing lattice" 
      lattice = init_ising_lattice(n)

    print "I donlt like the energy diff approach - may change this" 
    energy = 0
    energies = np.zeros(nsteps)
    def sumNeigh(lattice,i,j,n): 
        Sn = lattice[(i-1)%n,j]+lattice[(i+1)%n,j]+\
             lattice[i,(j-1)%n]+lattice[i,(j+1)%n]
        return Sn 


    print "WARNING: this needs to be initialized using actual energy ni a smarter way" 
    latticeEnergies = np.ones([n,n])*1e9
    for i in range(n):
      for j in range(n):
        S0 = lattice[i,j]
        Sn = sumNeigh(lattice,i,j,n) 
        energyCurr= energyij(S0,Sn,J,H)  
        latticeEnergies[i,j] = energyCurr 

   
    # simulator 
    for step in range(nsteps):
        # gen random i,j over range 
        i = randrange(n)
        j = randrange(n)
        # sums up the neighboring spins
        Sn = sumNeigh(lattice,i,j,n) 
        #dE = energydiff(lattice[i,j],Sn,J,H)
        S0 = lattice[i,j]
        ST = -S0 
        energyCurr= energyij(S0,Sn,J,H) 
        #energyCurr= latticeEnergies[i,j]    
        energyTrial = energyij(ST,Sn,J,H) 
        dE = energyTrial - energyCurr 

        # Metropolis criterion for accepting a spin flip  
        if dE < 0 or random() < exp(-dE/T):
            lattice[i,j] = -lattice[i,j]
            latticeEnergies[i,j] = energyTrial    
            energy += dE
        energies[step] = energy
    return lattice,latticeEnergies, energies

def saveImg(lattice,title=None,fname="ising.png"):
    # creates a snapshot image of the current state of the lattice
    plt.figure()
    print "add routine to make aspect = exact" 
    plt.pcolormesh(lattice,cmap='gray') 
    if title is not None:
      plt.title(title) 
    plt.gcf().savefig(fname)
    return 
    

def main():
    import sys,getopt
    opts,args = getopt.getopt(sys.argv[1:],'n:s:h:j:t:')
    n = 200
    nsteps = 500000
    H = 0
    J = 1
    T = 1
    for key,val in opts:
        if key == '-n': n = int(val)
        elif key == '-s': nsteps = int(val)
        elif key == '-h': H = float(val)
        elif key == '-j': J = float(val)
	elif key == '-t': T = float(val)
    lattice,energies = ising(n,nsteps,H,J,T)
    saveImg(lattice,title="T=%f"%T)
    plot(energies)
    return

def plot(energies):
    plt.plot(energies)
    plt.gcf().savefig("energies") 
    return

if __name__ == '__main__': main()
