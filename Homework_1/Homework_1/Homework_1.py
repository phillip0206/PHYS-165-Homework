#Homework #1 by Isaac Pliskin
#All problems are included
import numpy as np #importing numpy library for the arrays

#BEGIN PROBLEM 1
values = np.ones(100, int)  #creates an array of 100 ones

#this following bit isn't needed but will help make outputs better and less ugly
for x in range(len(values)):
    values[x] *= (x + 1) #sets the value at x in values to x

#print the 23rd and 46th items of values
#this should out put an array containing the integers between 23 to 46
print("Problem (1.a.):")
print(values[22:47], '\n')

#print the last 15 values of values
print("Problem (1.b.):")
print(values[len(values) - 16:len(values)], '\n')

new_values = np.empty([10,10], int) #create a new 10x10 array of ones

#there is absolutely an easier way to do this using the shape function but I can't figure it out
#it is also 21:48 so the garbage will do
for m in range(0,10,1):
    for n in range(0,10,1):
        new_values[m,n] = (m * 10) + (n + 1) #I feel like there is an easier way to do this

#prints the values in Row 2 to Row 4, Column 6 to Column 7
print("Problem (1.c.):")
print(new_values[1:5,5:7], '\n')

#BEGIN PROBLEM 2
first_name = input("What is your first name? ") #asks for and retrieves the user's first name
last_name = input("What is your last name? ") #asks for and retrieves the user's last name
age = int(input("How old are you? (in years) ")) #asks for and retrieves the user's age as an integer

age += 10 #adds ten years to the user's age

#prints the user's name followed by their age in ten years
print("\nProblem (2.a.):")
print("Hello {} {}. In 10 years you will be {} years old.\n".format(first_name, last_name, age))

#BEGIN PROBLEM 3
slicing_array = np.ones([20,20], float) #creates a 20x20 array that I am going to cut up

#there is absolutely an easier way to do this using the shape function but I can't figure it out
#it is also now 22:35 so the garbage will do
for m in range(0,20,1):
    for n in range(0,20,1):
        #each value will be set to m.n 
        #thus when it is output you can tell that a number is at position [m,n]
        slicing_array[m,n] = (m + 1) + ((n + 1) / 100) #I feel like there is an easier way to do this

print("The array is only 20x20")
num_rows = int(input("Enter number of rows to slice: ")) #asks for and retrieves the number of rows that will be sliced
num_cols = int(input("Enter number of cols to slice: ")) #asks for and retrieves the number of cols that will be sliced
start_row = int(input("Enter starting row: ")) #asks for and retrieves the starting row
start_col = int(input("Enter starting col: ")) #asks for and retrieves the starting col

#the following while loop makes sure that someone doesn't try to print out 23 rows of a 20 row matrix
while (num_rows + start_row > 21) and (num_cols + start_col > 21):
    print("THE HUMAN HAS MADE AN ERROR FIX IT NOW (index out of range)") #yells at the user for making a mistake
    num_rows = int(input("Enter number of rows to slice: ")) #asks for and retrieves the number of rows that will be sliced
    num_cols = int(input("Enter number of cols to slice: ")) #asks for and retrieves the number of cols that will be sliced
    start_row = int(input("Enter starting row: ")) #asks for and retrieves the starting row
    start_col = int(input("Enter starting col: ")) #asks for and retrieves the starting col

#this will print the section asked for
print("\nProblem (3.a.):\n")
for m in range(start_row - 1, start_row + num_rows - 1):
    print("[ ", end="") #begins the row
    for n in range(start_col - 1, start_col + num_cols - 1):
        print("{0:05.2f}".format(slicing_array[m, n]), end=" ") #prints the value with a space after it with some formatting
        #in the formatting I have done the following (in order that they appear:
        #0 is the placeholder
        #0 indicates pad with zeros
        #5 indicates the minimum length (including the decimal) is 5, e.g. mm.nn 
        #remember that in the array the number before the decimal is the row and after is the column
        #2 indicates the precision
        #f makes sure it is a float
        #this makes the array real pretty if you print the whole thing out
    print("]\n") #ends the row