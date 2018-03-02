# Homework 3 for Physics 165 by Isaac Pliskin
from numpy import sqrt, cos, sin, pi # to do the math

def taxicab(point_a, point_b, mode): # point_a and point_b should be lists with two entries, mode is an integer
    '''This is the function to be used in Problem 1.
       It takes in the starting and ending point and computes the distance.
       This is either done using geometry or by doing simple math.
    '''
    if mode: # if mode != 0 basically
        d_x = point_b[0] - point_a[0] # the difference in x values
        d_y = point_b[1] - point_a[1] # the difference in y values
        D = sqrt(d_x**2 + d_y**2) # find the length of the straight line between the two points
    else: # if mode is zero
        D = abs(point_b[0]-point_a[0]) + abs(point_b[1] - point_a[1]) # find the total number of blocks travelled
    return D # returns the value of the distance

def R(r, t):
    '''This is the function to be used in Problem 2.
       It rotates a vector.
    '''
    R_matrix = [[cos(t*pi/180), -sin(t*pi/180)], # the first row of the rotation matrix
                [sin(t*pi/180), cos(t*pi/180)]] # the second row of the rotation matrix

    r_prime = [r[0] * R_matrix[0][0] + r[1] * R_matrix[0][1], r[0] * R_matrix[1][0] + r[1] * R_matrix[1][1]] # does matrix multiplication the right way because Python is dumb
    # sorry python.

    return r_prime # returns the new and improved vector optimus prime I mean r_prime

# Begin Problem 1
start = [0, 0] # initialize the vector start
end = [0, 0] # initialize the vector end

start[0] = float(input("Please enter starting x value: ")) # retrieve the x value of start from the user
start[1] = float(input("Please enter starting y value: ")) # retrieve the y value of start from the user
end[0] = float(input("Please enter ending x value: ")) # retrieve the x value of end from the user
end[1] = float(input("Please enter ending y value: ")) # retrieve the y value of end from the user

choice = int(input("Enter 1 for actual distance, 0 for blocks: ")) # let the user think they have free will

print(taxicab(start, end, choice)) # print the result from the taxicab function

# Begin Problem 2
x = float(input("Please enter the x coord: ")) # ask the user for an x coordinate
y = float(input("Please enter the y coord: ")) # ask the user for a y coordinate
theta = float(input("Please enter the rotation angle in degrees: ")) # ask the user for the degrees of rotation to do

_,y = R([x,y], theta) # set y equal to the y value of r_prime being returned. _ is a dummy variable and gets ignored afterwards

print(y) # print the y value