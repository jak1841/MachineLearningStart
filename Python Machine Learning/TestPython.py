import random
import matplotlib.pyplot as plt
import numpy as np
#This Project will illustrate my skills at matplotlib and gradient descent

#LearningRate
learningrate = .01

#We have a function y = (x - 5) + 9 and we will figure out the lowest value using gradient descent by picking a random x value
def function(x):
    return (x-5)**2 + 9

#Derivative of the function at x
def derivativefunction(x):
    return 2*(x-5)

#Finds gradient using x = x - learningrate(dy/dx)
def findGradient(x):
    #Gives us the y of the function at x at the beginning
    y = function(x)

    for z in range(1000):
        #Choose Direction of steepest descent by looking at derivative
        x = x - (learningrate*derivativefunction(x))

    print(y)
    print(function(x))

findGradient(10000)

#This all was taken by scriptverse
# 100 linearly spaced numbers
x = np.linspace(0,30,10)

# the function, which is y = x^2 here
y = (x-5)**2 + 9

# # setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x,y,'r')

# show the plot
plt.show()
