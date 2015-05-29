# -*- coding: utf-8 -*-
"""
Created on Wed May 27 08:49:13 2015

@author: Jonathan Adams

Attempting Numerical solution on simple particle moving at constant velocity
This helped:
phys.csuchico.edu/ayars/312/Handouts/comp-phys-python.pdf

"""

import matplotlib.pyplot as plt
import numpy as np
import math

def constantV(): 
   N = 100                #number of steps
   y0 = 0                 #initial position
   vel0 = 10               #m/s
   tau = 1                #total simulation time (s)
   dt = tau/float(N-1)    # time step  
   time = np.linspace(0,tau,N)
   pos = np.zeros(N)      #array holding positions
   vel = pos + vel0       #array holding velocities
   pos[0] = y0   
   for i in range(0,len(pos)-1):
       pos[i+1] = euler(pos[i],dt, vel[i])
   
   plt.plot(time, pos)
    # runs main code
   return;
"""
Simple Euler Method
"""
def euler( y, dt, deriv):
    fn_next = y + deriv*dt
    return fn_next
    
"""
Euler Method expanded as a taylor expansion. 
fns is a list of functions, f(x), f'(x), f''(x)... 
Can use as many derivatives as desired.
"""
def euler2( fns, dt ):
    fnNext = 0
    for i in range(0,len(fns)):
        fnNext += fns[i] * pow(dt, i) / math.factorial(i)
    return fnNext
    
def constantA():
    N = 1000
    y0 = 0
    vel0 = 0
    accel = 10
    tau = 1
    dt = tau/float(N-1)
    time = np.linspace(0,tau,N)
    pos = np.zeros(N)
    acc = pos + accel    
    vel = pos + (vel0+accel*time)
    pos[0] = y0
    pos2 = pos
    for i in range(0,len(pos)-1):
        pos[i+1] = euler(pos[i],dt,vel[i])
        pos2[i+1] = euler2([pos[i],vel[i],acc[i]],dt)
        
    plt.plot(time,pos)
    plt.plot(time,pos2)
    plt.plot(time,5*time*time)
    plt.xlabel("time")
    plt.ylabel("position , velocity")
    plt.show()
    return;
    
def changingA():
    N = 100
    y0 = 0
    vel0 = 0
    acc0 = 0
    jer0 = 10    
    tau = 1
    dt = tau/float(N-1)
    time = np.linspace(0,tau,N)
    pos = np.zeros(N)
    jer = pos + jer0
    acc = pos + (acc0 + jer*time)    
    vel = pos + (vel0 + 0.5*jer*time*time)
    pos[0] = y0
    pos2 = pos
    for i in range(0,len(pos)-1):
        pos[i+1] = euler(pos[i],dt,vel[i])
        pos2[i+1] = euler2([pos2[i],vel[i],acc[i],jer[i]],dt)
    
    acc3 = np.zeros(N)
    vel3 = np.zeros(N)
    pos3 = np.zeros(N)
    
    """
    Ran into a strange bug here. If i say vel3 = acc3 and pos3 = acc3, 
    then euler method will return only zeros.

    """
    for i in range(0,len(pos)-1):
        acc3[i+1] = euler(acc3[i],dt,jer[i])
    for i in range(0,len(pos)-1):        
        vel3[i+1] = euler(vel3[i],dt,acc3[i])
    for i in range(0,len(pos)-1):        
        pos3[i+1] = euler(pos3[i],dt,vel3[i])
        
#    plt.plot(time,pos)
    plt.plot(time,pos2)
    plt.plot(time,pos3)
    plt.xlabel("time")
    plt.ylabel("position , velocity")
    plt.legend()
    plt.show()
    return;