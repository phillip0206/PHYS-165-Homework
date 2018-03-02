# Physics 165 Lab 1
# Isaac Pliskin, Luis Argueta, Laura Ocampo, Zixi Zhang
from matplotlib import pyplot # for graphing all the stuff
from csv import reader # we need this to use the files
import numpy as np # we need this to do math

def V(t, A, tau): # V(t) function to be used later on
    output = A*(1-np.exp(-t/tau)) # the function
    return output # return the value

def W(t, A, tau): # W(t) function to be used
    output = A*(np.exp(-t/tau) - 1 + (t/tau)) # the function
    return output # return the value

t_values = np.arange(0, 2, 0.02 )
V_values = [[], [], [], [], [], []]
W_values = [[], [], [], [], [], []]

v_t_values = t_values * 3.5
w_t_values = t_values * 15

for i in np.arange(0, 6):
    A, tau = i + 1, i+ 1
    for t in v_t_values:
        V_values[i].append(V(t, A, tau))
    for t in w_t_values:
        W_values[i].append(W(t, A * 0.01, (0.5 * tau)**2))

V_data = [[], []]
W_data = [[], []]

with open("bg1.csv") as v_input, open("bg2.csv") as w_input:
    v_reader = reader(v_input, delimiter=',')
    w_reader = reader(w_input, delimiter=',')

    for v_line in v_reader:
        if v_line:
           V_data[0].append(v_line[0])
           V_data[1].append(v_line[1])

    for w_line in w_reader:
        if w_line:
            W_data[0].append(w_line[0])
            W_data[1].append(w_line[1])

for i in np.arange(0, 6):
    pyplot.figure("Vees")
    pyplot.plot(v_t_values, V_values[i], marker="o", linestyle='None', label="V{}".format(i))
    pyplot.figure("Yews")
    pyplot.plot(w_t_values, W_values[i], marker="*", linestyle='None', label="W{}".format(i))

pyplot.figure("Vees")
pyplot.plot(V_data[0], V_data[1], marker="s", linestyle='None', label="V data")
pyplot.legend(loc=0, fontsize=24)
pyplot.title("V(t)", fontsize=24, fontname="Comic Sans MS")
pyplot.xlabel("time in hours", fontsize=24, fontname="Comic Sans MS")
pyplot.ylabel("population in bacteria", fontsize=24, fontname="Comic Sans MS")

pyplot.figure("Yews")
pyplot.plot(W_data[0], W_data[1], marker="D", linestyle='None', label="W data")
pyplot.legend(loc=0, fontsize=24)
pyplot.title("W(t)", fontsize=24, fontname="Comic Sans MS")
pyplot.xlabel("time in hours", fontsize=24, fontname="Comic Sans MS")
pyplot.ylabel("population in bacteria", fontsize=24, fontname="Comic Sans MS")

pyplot.show()