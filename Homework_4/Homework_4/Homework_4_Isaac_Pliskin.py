# Homework 4 for PHYS165 by Isaac Pliskin
# Due Monday, March 5th, 2018
from numpy import exp, arange, abs, array
from numpy.linalg import solve
from matplotlib import pyplot
import scipy.integrate as integrate
import scipy.optimize as so

# Begin Problem 1
def simpsons(f, a, b, n):
    h = (b - a)/(n) # calculate h
    # since n = 10, we will only get 5 intervals which gives a really bad approximation

    sum1 = 0 # initialize first sum (will be multiplied by 2 later)
    sum2 = 0 # initialize second sum (will be multiplied by 4 later)

    for i in range(1, n - 1): # sum through all the values that will be multiplied by 2
        sum1 += f(2*h*i + a) # add f(2hi + x1) where x1 = a to the first sum

    for i in range(1, n): # sum through all the values that will be multiplied by 4
        sum2 += f(h*(-1 + 2*i) + a) # add f(h(-1+2i) + x1) wherw x1 = a to the second sum

    simps = (h/3)*(f(a) + 2*sum1 + 4*sum2 + f(b)) # add f(x1), 2sum1, 4sum2, and f(x2) where x1 = a and x2 = b

    return simps # return the computed value

a, b, n = 0, 10, 10 # a, b, and n values for the problem
f = lambda x : exp(-(x**2)) # define the function to be integrated

# Trapezoidal rule

sum_tr = 0
dx = (b - a)/n # the step value for the trapezoidal rule

for i in arange(start = a+1, stop = b+dx, step = dx): # run through all the points in the interval
    # if I do not go to b+dx then the value of b will be skipped
    sum_tr += (dx/2)*(f(i-1) + f(i)) # add f(xi-1) and f(xi) time (dx/2) to the sum


print("Using the trapezoidal rule, exp(-x^2) = ", sum_tr) # print the sum

# Simpson's rule
sum_sr = simpsons(f, 0, 10, 10) # use the fucntion defiend above
# thanks to using n = 10, the result will be rather far off.

print("Using Simpson's Rule, exp(-x^2) = ", sum_sr) # print the value of the simpson's rule

# I am not sure how to exactly compute the error of the two methods above

integral, error = integrate.quad(f, 0, 10) # use built in quadrature methods
print("Using SciPy, the integral is: ", integral, " with an error of: ", error) # print the value of the integral plus the error

# Begin Problem 2
A = array([[-1, -3, 5, 10],
              [2, 7, 7, 1],
              [5, 5, 1, 2],
              [2, 3, 7, 1]]) # define the coefficient matrix from Problem 2

b = array([-10, 7, 1, 1]) # define lambda

x = solve(A, b) # solve the system of Ax=b for x

print("The solution to Ax=b is: ",  x) # print the result

g = lambda x : x**3 - x + 1 # define the nonlinear function to be solved

x = arange(-2, 2, 0.1) # define a range of x values to go over

pyplot.figure(1) # make a new plot
pyplot.plot(x, g(x)) # plot g(x) vs. x

pyplot.show(block=False) # I have to do this so that the following lines will show up even as the graph is displayed

print("The root seems to be between x = -2 and x = -1") # I used an educated guess

pyplot.axvline(-2, color = "red", linestyle = '--') # for added flair, display the left boundary of my guess
pyplot.axvline(-1, color = "red", linestyle = '--') # for added flair, display the right boundary of my guess

x_sol = so.fsolve(g, [-2, -1]) # solve for x

print("The solution to the equation is: ", x_sol) # print the solution

pyplot.plot(x_sol, g(x_sol), 'bo') # plot the point for dramatic effect
michael_scott = pyplot.gca() # take over forcefully
michael_scott.set_title("y = x^3 - x + 1", fontsize = 24) # set the title of the grpah and make it 24 pt font
michael_scott.set_xlabel("x values") # label the x axis
michael_scott.set_ylabel("y values") # label the y axis
pyplot.axhline(0, color="black", linestyle = "--") # add in the horizontal origin line because I like having it
pyplot.axvline(0, color="black", linestyle = "--") # add in the vertical origin line because I like having it

pyplot.show() # finally show the plot