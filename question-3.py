#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import math
from matplotlib import pyplot as plt

# initializing variables acc to given initial value y(0)=1
x_initial = 0
y_initial = 1
n = 0 # iterator 


# the following function simply returns y, because in this question
# we have y' = y
def function(x, y):
    return y;


#after manually solving the DE, y' = y, we get y = e^x, hence we will write a 
#function that returns the value of e^x, by inputting x
def expo(x):
    return math.exp(x)



# a function that returns the value of y, at the last iteration, using Euler's Method
def eulersCalculation(h_value):
    print("  ***  For h = ", h_value, "  ***  ")
    y_temp = 1
    x_temp = 0
    h1=0
    
    list_x_values = [] #initializing list of x values with initial value of x, we'll append new values inside the loop
    list_y_values = [] #initializing list of y values with initial value of y, we'll append new values inside the loop
    list_iterator = [] #values of the iterator of Euler's Calculation
    list_actual_y_vals = []
    
    iterations = int((1 - x_temp) / h_value)
    
    for n in range(0, iterations+1):     
        y_final = y_temp + h1 * function(x_temp, y_temp)
        x_temp += h1
        round(x_temp, 4)
        y_temp = y_final
        round(y_final, 4)
        h1 = h_value #assigning value of h = 0.1 to it, for all the coming iterations
        
        list_iterator.append(n)
        list_x_values.append(round(x_temp, 4))
        list_y_values.append(round(y_final,4))
        list_actual_y_vals.append(round(expo(round(x_temp, 4)), 4))
        
    df = pd.DataFrame({' x_i  ' : list_x_values, ' y_num  ' : list_y_values, 'y-actual' : list_actual_y_vals})
    print(df)
    
    st = "y-num(h = )", h_value
    
    
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(list_x_values,list_y_values ,'g--', label=st)    
    return [list_x_values,list_actual_y_vals]

arr=eulersCalculation(0.1)

eulersCalculation(0.05)

plt.plot(arr[0],arr[1],'b--', label="y-exact ")
plt.legend()


# In[ ]:





# In[ ]:




