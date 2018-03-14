# Laura Ocampo, Isaac Pliskin, Luis Argueta, Zixi Zhang, Phillip Cho
# Physics 165 Lab 2
# The one with the random walks
from numpy.random import random as rng
import numpy as np
import matplotlib.pyplot as plt

num_steps=1000

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
plt.show()

