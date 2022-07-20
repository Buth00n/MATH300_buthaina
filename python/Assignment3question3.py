

import matplotlib.pyplot as thatplot
import numpy as np

def function3(N, x=[]):    
    xtotals = []
    for i in range(len(x)):
        total = 0
        for n in range(1,N+1):
            total += ((np.power(n,x[i])) / (n))
            
        xtotals.append(total)
        #return xtotals
    
    thatplot.plot(x,xtotals)