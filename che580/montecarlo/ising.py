#!/usr/bin/env python
import numpy as np 
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pylab as plt 
"""
Bare bones ising model 

Something seems a bit buggy still, so work in progress 
"""

from math import exp
from random import randrange,choice,random
from numpy import zeros

# initialize random lattice 
def initIsingLattice(n):
    rands= np.reshape(np.random.rand(n*n),[n,n]) 
    #print rands 
    lattice = np.ones([n,n],dtype=int) 
    lattice[ rands>0.5 ] = -1
    #print lattice 

    return lattice

# score entire lattice
# This is a terrible approach; the scoring can definitely be vectorized
# but I couldn't think of a way to do this for an arbitrary scoring
# function using nearest-neighbors that wrap
def scoreIsingLattice(lattice,n,J,H):
    latticeEnergies = np.ones([n,n])*1e9
    for i in range(n):
      for j in range(n):
        S0 = lattice[i,j]
        Sn = sumNeigh(lattice,i,j,n) 
        energyCurr= energyij(S0,Sn,J,H)  
        latticeEnergies[i,j] = energyCurr 
    return latticeEnergies

# sum nearest neighbors
def sumNeigh(lattice,i,j,n): 
  Sn = lattice[(i-1)%n,j]+lattice[(i+1)%n,j]+\
    lattice[i,(j-1)%n]+lattice[i,(j+1)%n]
  return Sn 

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

    # Initialize lattice 
    if lattice is None: 
      print "Initializing lattice" 
      lattice = initIsingLattice(n)


    # Get initial energy for all elements in lattice 
    latticeEnergies = scoreIsingLattice(lattice,n,J,H)

   
    # simulator 
    energy = 0
    energies = np.zeros(nsteps)
    for step in range(nsteps):
        # gen random i,j over range 
        i = randrange(n)
        j = randrange(n)

        ## Evaluate energy of point i,j
        # sums up the neighboring spins
        Sn = sumNeigh(lattice,i,j,n) 
        #dE = energydiff(lattice[i,j],Sn,J,H)
        S0 = lattice[i,j]
        ST = -S0 
        energyCurr= energyij(S0,Sn,J,H) 
        #energyCurr= latticeEnergies[i,j]    
        energyTrial = energyij(ST,Sn,J,H) 
        dE = energyTrial - energyCurr 

        ## Metropolis criterion for accepting a spin flip  
        if dE < 0 or random() < exp(-dE/T):
            lattice[i,j] = -lattice[i,j]
            latticeEnergies[i,j] = energyTrial    
            energy += dE

        ## score system energy 
        energies[step] = energy
    return lattice,latticeEnergies, energies

def saveImg(lattice,title=None,fname="ising.png"):
    # creates a snapshot image of the current state of the lattice
    plt.figure()
    ax = plt.subplot(111) 
    ax.pcolormesh(lattice,cmap='gray') 
    if title is not None:
      ax.set_title(title) 
    ax.axis('equal')
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
    lattice,latticeEnergies,energies = ising(n,nsteps,H,J,T)

    saveImg(lattice,title="T=%f"%T)
    plot(energies)
    return

def plot(energies):
    plt.plot(energies)
    plt.gcf().savefig("energies.png") 
    return

if __name__ == '__main__': main()
