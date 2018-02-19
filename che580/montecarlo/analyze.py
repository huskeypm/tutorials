import numpy as np 
def getStats(lattice,latticeEnergies,T):
    # average magnetization
    M = np.mean(lattice)
    #print M

    # average energy
    E = np.mean(latticeEnergies)
    #print E

    # specific heat
    EE = latticeEnergies*latticeEnergies
    EE = np.mean(EE)
    cv = (EE - E**2)/T**2
    #print cv
    
    return (M,E,cv)

