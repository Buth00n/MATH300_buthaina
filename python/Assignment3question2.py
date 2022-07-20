

import matplotlib.pyplot as thisplot

def function_N(N):    
    sum1 =[]

    for n in range(1,N+1):
        sum1.append(((-1)**(n+1))*(1/n))
        
    #return sum1
    
    
    thisplot.plot(sum1)
    
