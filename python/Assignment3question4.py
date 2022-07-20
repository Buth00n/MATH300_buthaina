import matplotlib.pyplot as hahaanotherplot
import numpy as np
def midpoint(f, a=0, b=1, n=100):
    h = (b-a)/n
    integral = 0
    for i in range(n):
        integral += f((a + h/2.0) + i*h)
    integral *= h
    return integral
  


def midpointplot(f, a=0, b=100, n=1000):
    h = (b-a)/100
    h2 = (b-a)/n
    x = np.arange(a,b+h,h)
    hahaanotherplot.plot(x,f(x))
    
    midpointnx = np.arange(a,b,h2)
    hahaanotherplot.bar(midpointnx,f(midpointnx), facecolor='orange', width=h, alpha=0.5)
    hahaanotherplot.xlim(a,b)
    hahaanotherplot.show()
    
def function(x):
    return x**2 + 1
a = midpoint(function)  
print(midpoint(function))