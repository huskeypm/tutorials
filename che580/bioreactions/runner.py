# import pythons random number generator
# NOTE: for production code you need to make sure to have
# a very good random number generator.
#from helper import *
from helper import *
import random 
import math
import numpy as np



################################################################
# start of main simulation
################################################################

def main(
    # parameters
    A0 = 30110, # initial molecule count for species A
    B0 =     0, # initial molecule count for species B
    C0 =     0, # initial molecule count for species C
    k1 = 0.024e5,           # forward rate [#/(Mol*s)]
    k2 = 0.015e5,           # backward rate [1/s]
    volume = 5e-20,         # reaction volume [L]
    maxTime = 1.0e-2,   # maximum simulation time [s]
    outputFreq = 1000,                            # output frequency
    verbose = False
):

    # initialize time, random number generator,
    # initial molecule counts, and molecule count update
    # functions
    random.seed(124213)
    N_avo  = 6.0221415e23  
    time       = 0.0
    iteration  = 0 # iteration count
    molCounts  = [A0,B0,C0]
    rates      = [k1/volume/N_avo, k2]           # need to convert 
    #print molCounts, rates
    updaters   = [react1_updater,react2_updater]

    # open output files
    fileHandles = open_output_files() 
    results = dict()
    results["time"]=[]
    results["molCounts"]=[]
    results["molConcs"]=[]
    
    # we simulate until we hit our maximum simulation time
    while time < maxTime:
    #for i in np.arange(10000):
        
        # compute the propensities a_i for each reaction
        # and the sum a_0
        a_i = compute_propensities(molCounts, rates)
        a_0 = sum(a_i)
        #print a_i

        # pick a random number, compute the time increment
        # and update t (equation 21a in Gillespie's paper)
        rand_1 = random.random()
        #print rand_1
        tau    = 1.0/a_0 * math.log(1/rand_1)
        time  += tau

        # find the reaction to execute (equation 21b in
        # Gillespie's paper). We need a second random number
        # here. We don't really need the while loop here since
        # we only have two possible reactions but we do it anyway
        # to keep it more general. 
        rand_2    = random.random()
        threshold = a_0 * rand_2
        
        summation = 0
        count     = 0
        while threshold > summation:
            summation += a_i[count]
            count += 1
            
        # update molecule counts by calling the proper updater
        # function. Note, arrays in python are zero index based
        # hence we need count-1 to access the proper updater.
        molCounts = updaters[count-1](molCounts)

        # dump data every outputFreq iteration
        # we also print a short progess message 
        if (iteration % outputFreq) == 0:
            if verbose: 
              print "iteration %d   time %5.4g" % (iteration, time)  
            
            # store 
            results["time"].append(time)
            molCts = np.copy(molCounts)
            molConcs = molCts/volume/N_avo
            results["molCounts"].append(molCts)
            results["molConcs"].append(molConcs)
            #print molCounts
            #print "###",results["molCounts"]
            write_data_to_output(fileHandles, time, molConcs)

        iteration += 1    

    
    # cleanup
    close_output_files(fileHandles)


    # reformat
    for key in results.keys():
      results[key] = np.asarray( results[key] )
   
    return results       

