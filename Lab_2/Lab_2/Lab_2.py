# Laura Ocampo, Isaac Pliskin, Luis Argueta, Zixi Zhang, Phillip Cho
# Physics 165 Lab 2
# The one with the random walks
from numpy.random import random as rng
import numpy as np
import matplotlib.pyplot as plt

"""num_steps=1000

x_i,y_i=0,0
x=[]
y=[]
pos_final=[[],[]]

for i in range (0,1000):
    x_samples=rng(1000)
    y_samples=rng(1000)
    for i in range(0, 1000):
        if x_samples[i] < 0.5:
            x.append(1)
        else:
            x.append(-1)
        if y_samples[i] < 0.5:
            y.append(1)
        else:
            y.append(-1)
    x_final=sum(x)
    y_final=sum(y)
    pos_final[0].append(x_final)
    pos_final[1].append(y_final)
    
for i in range(0,1000):
    pos=np.sqrt((pos_final[0][i])**2+(pos_final[1][i])**2)
    print(pos)
    # plot(pos)
    
plt.scatter(pos_final[0],pos_final[1])
plt.hist(pos,num_steps)
plt.show()"""

x = np.zeros(1000)
y = np.zeros(1000)



for i in range(0, 1):
    x_samples = rng(1000)
    y_samples = rng(1000)

    for i in range(1, 1000):
        if x_samples[i] < 0.5:
            x[i] = x[i - 1] + 1
        else:
            x[i] = x[i - 1] - 1

        if y_samples[i] < 0.5:
            y[i] = y[i - 1] + 1
        else:
            y[i] = y[i - 1] - 1

    """plt.figure("No Line Plot")
    plt.plot(x, y)
    plt.figure("Line Plot")
    plt.plot(x, y, '--')
    plt.figure("Scatter")
    plt.scatter(x, y, s=2)"""
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
    ax1.plot(x, y)
    ax1.set_title('Normal Plot')
    ax2.scatter(x, y, s=2)
    ax2.set_title('Normal Scatter')
    ax3.scatter(x, y, color='r')
    ax3.set_title('I Don\'t Know How To Omit This')
    ax4.plot(x, y, '--')
    ax4.set_title('Plot But With Dashed Lines')

plt.show()