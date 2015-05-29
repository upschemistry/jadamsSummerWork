# -*- coding: utf-8 -*-
"""
Created on Thu May 28 09:07:40 2015

@author: Jonathan Adams

"""
import matplotlib.pyplot as plt
import numpy as np
import math
import time
#import multiprocessing as mp

def main():
    sec1 = time.time()
    Nx = 1000                           # number of points not including zero
    L = 1                              # length
#    d = .0001
    x = np.linspace(0,L,Nx+1)          # creating x
#    dx = x[1]-x[0]
#    dt = 0.01                           # time step
#    constant = d*dt/dx**2
    constant = 0.2
    fn = np.zeros(Nx+1)
    for i in range(0,len(fn)):
        fn[i] = makeFunction(x[i])
    plt.plot(x,fn)
       
    for i in range(0,1001):               # number of time steps
        fn = diffuse(fn, constant)
#        if i%1000 == 0:
#            plt.plot(x,fn-i/10000.)
                  
    plt.plot(x,fn-.5)
    sec2 = time.time()
    print "Total Time:", sec2-sec1, "seconds"
    

def makeFunction( x ):
    y = math.sin(math.pi * x) + 0.1 * (math.sin(100 * math.pi * x))
    return y;
    
    
    
"""
# I think this is slower because it has to restart the pool process
# every time the function is called. It has to do work in order to divide up
# the work into several processes every single time.
# I would need to somehow code it so the pool process is only called once 
# (at the for loop in Main method). Problem with that is it will try to compute
# multiple integers of the for loop at once, which is not good because each 
# iteration requires data from the previous
# So parallel programming is out for the moment
   
def diffuse(x, constant, pool):
    y = x
    length = len(x)
    #pool = mp.Pool(processes = 5)
    results = [pool.apply(eulerD, args=(x[i-1],x[i],x[i+1],constant,)) for i in range(1,length-1)]
    pool.close()
    for i in range(1,length-1):
        y[i]= results[i-1]
    
    # Boundary Conditions 
    y[0] = 0
    y[len(x)-1] = 0        
        
    return y    

def eulerD(xlow, x, xupp, constant):
    return x + constant * (xupp - 2 * x + xlow)

"""    
def diffuse(x, constant):
    y = x
    for i in range(1,len(x)-1):
        y[i] = x[i] + constant * (x[i+1] - 2*x[i] + x[i-1])
    # Boundary Conditions 
    y[0] = 0
    y[len(x)-1] = 0        
        
    return y
    
    