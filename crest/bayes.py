import numpy as np 
def flipper(nRolls = 10, mode="A",bias=0.77):
  if mode is "C": # biased coin 
    thresh = bias
  else: 
    thresh = 0.5
  nRolls = np.int(nRolls)
  # random draws
  rolls = np.random.rand(nRolls)  
  
  # all heads 
  outcomes = ['t']*nRolls
    
  # apply thresh 
  tails = np.ndarray.flatten(np.argwhere(rolls < thresh))
  
  #print rolls
  for i in tails:
        outcomes[i] = 'h'

  return outcomes 

def countHeadsTails(outcomes):
    count = [1 if s is 'h' else 0 for s in outcomes]
    count = np.asarray(count)
    hs = np.sum( count )
    ts = np.shape(count)[0] - hs
    return hs, ts

