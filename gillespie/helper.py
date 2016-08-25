#############################################################
# helper functions
#############################################################

def react1_updater(molCount):
    """
    This function updates the molecule count should reaction
    number 1 happen. Input parameter is the list of current
    molecule counts and we return the new molecule counts.
    """

    molCount[0] -= 1      # update A
    molCount[1] -= 1      # update B
    molCount[2] += 1      # update C

    return molCount



def react2_updater(molCount):
    """
    This function updates the molecule count should reaction
    number 2 happen. Input parameter is the list of current
    molecule counts and we return the new molecule counts.
    """

    molCount[0] += 1      # update A
    molCount[1] += 1      # update B
    molCount[2] -= 1      # update C

    return molCount


def compute_propensities(molCount,rates):
    """
    This function returns the reaction propensities according
    to the current molecule counts (step 1 on 2345 in Gillespie's
    paper 1977 paper). Since we have two reactions we return
    a list with two values. Per definition of the propensities
    in Gillespie's paper we return the propensity k1*A*B for 
    reaction 1 and k2*C for reaction 2 where A, B, and C are the 
    instantaneous molecule counts and k1, k2 the reaction rates.
    """
    
    return (rates[0]*molCount[0]*molCount[1], rates[1]*molCount[2])    
    


def open_output_files():
    """
    This function opens the output files and returns file
    handles to each.
    """

    outfile_A = open("A.dat","w")
    outfile_B = open("B.dat","w")
    outfile_C = open("C.dat","w")

    return [outfile_A, outfile_B, outfile_C]



def write_data_to_output(fileHandles, time, data):
    """
    This function writes a (time, data) pair to the
    corresponding output file. We write concentrations
    not molecule counts.
    """

    for i in range(0,len(fileHandles)):
        fileHandles[i].write("%5.4e  %8.7f\n" %(time, data[i]))
    


def close_output_files(fileHandles):
    """
    This function closes all output files.
    """

    for i in range(0,len(fileHandles)):
        fileHandles[i].close()
    

    
    

