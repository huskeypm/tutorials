
# coding: utf-8

# Adapt from http://code.activestate.com/recipes/577263-numerical-integration-using-monte-carlo-method/

# In[31]:

# Numerical Integration using Monte Carlo method
# FB - 201006137
import math
import random
import numpy as np 


# ### Function to integrate

# In[49]:

def f(x):
    return math.sin(x)
    #return math.sin(x)*math.exp(-x)


# In[50]:

# define any xmin-xmax interval here! (xmin < xmax)
xmin = 0.0
xmax = 2.0 * math.pi

# find ymin-ymax for corresponding xmin/xmax
numSteps = 1e3 # bigger the better but slower!
ymin = f(xmin)
ymax = ymin
for i in range(np.int(numSteps)):
    x = xmin + (xmax - xmin) * float(i) / numSteps
    y = f(x)
    if y < ymin: ymin = y
    if y > ymax: ymax = y
#print ymin, ymax        


# ### Monte Carlo

# In[62]:

rectArea = (xmax - xmin) * (ymax - ymin)
numPoints = 1e4 # bigger the better but slower!
ctr = 0
p = [] # for storing data 
n = []
for j in range(np.int(numPoints)):
    x = xmin + (xmax - xmin) * random.random()
    y = ymin + (ymax - ymin) * random.random()
    if math.fabs(y) <= math.fabs(f(x)):
      if f(x) > 0 and y > 0 and y <= f(x):
        ctr += 1 # area over x-axis is positive
        p.append([x,y])
      if f(x) < 0 and y < 0 and y >= f(x):
        ctr -= 1 # area under x-axis is negative
        n.append([x,y])

fnArea = rectArea * float(ctr) / numPoints
monteCarloResult = fnArea
print "Numerical integration = " + str(monteCarloResult)


# ### Numerical comparison 

# In[63]:

import scipy.integrate as integrate
result = integrate.quad(lambda x: f(x), xmin, xmax)
#print result 
numpyResult = result[0]
print "Error", abs( monteCarloResult - numpyResult )


# ### Compare results 

# In[52]:

n = np.asarray(n)
p = np.asarray(p)
xs = np.linspace(xmin,xmax,200)
fvec = np.vectorize(f)


#plt.scatter(n[:,0],n[:,1],color='r')
#plt.scatter(p[:,0],p[:,1], color='b')
#plt.plot(xs,fvec(xs))


# In[ ]:



