# Homework #2 for Physics 165 by Isaac Pliskin
# Working with inputting and outputting files
# The data file is data1.txt
# output files should be Mult_2.txt and Sqrt_Col2.txt
from numpy import array, sqrt, tanh, sin, pi, arange # needed for creating arrays and taking square roots
from csv import reader # I need this to be able to skip lines
from matplotlib import pyplot # I don't want to name it anything because I prefer the name PyPlot

# Begin Problem 1
data_points = [[], []] # two dimensional list to hold both columns of data
with open("data1.txt", "r") as file: # opens the file
    file_data = reader(file, delimiter='\t') # create a csv.reader object with the file I have opnened, data is separated by spaces

    print(file.readline()) # skips the first line and prints it to the console
    for line in file_data: # go through all the lines in the csv reader object (skipping the first line)
        if line: # I need this because computers are dumb and if you have more than one blank line at the end of the document it kills everything
            # basically if the line is blank it will be skipped
            print(line) # print the line to the console to make sure everything goes well
            data_points[0].append(float(line[0]) * 2) # I add the first column times two to the first list in the list of lists
            data_points[1].append(sqrt(float(line[1]))) # I add the square root of the second column to the second list in the list of lists
        else: # If the line is blank....
            print("There is a blank line at the end of the file and as a stupid computer I don't know how to handle these.") # Insult the computer because I am frustrated.

column_one = array(data_points[0]) # create an array of the first column. Not a big fan of my naming scheme here
column_two = array(data_points[1]) # create an array of the second column. Still not a fan of the name

print("First array is: ", column_one) # Print the first array to make sure everything is still doing what it should be
print("Second array is: ", column_two) # Print the second array so it doesn't feel left out

with open("Mult_2.txt", "w") as output: # Open the first output file in write mode
    for item in column_one: # go through each item in the first array
        output.write("{}\n".format(item)) # write each item to the output file, with a new line after each item
    print("First array saved as Mult_2.txt") # Tell the user that the computer did its job (for once)

with open("Sqrt_Col2.txt", "w") as output: # Open the second output file in write mode
    for item in column_two: # go through each item in the second array
        output.write("{}\n".format(item)) # write each item to the output file, with a new line after each item
    print("Second array saved as Sqrt_Col2.txt") # Tell the user that the computer has successfully done two jobs, which is a first

# Begin Problem 2
x = arange(-4*pi, 4*pi, 0.1) # range of x values

pyplot.figure(1) # create the figure for the plot to live in
pyplot.plot(x, tanh(x), label = "tanh(x)") # plot the graph of tanh(x) with the label of tanh(x)
pyplot.plot(x, sin(x), label = "sin(x)", linestyle = '--') # plot the graph of sin(x) with the label of sin(x) and the style of dashes

michael_scott = pyplot.gca() # create the manager of the graph that is being shown
michael_scott.set_title("Tanh(x) & Sin(x)", fontsize = 24) # set the title of the grpah and make it 24 pt font
michael_scott.set_xlabel("x values") # label the x axis
michael_scott.set_ylabel("y values") # label the y axis
michael_scott.legend(loc = 4) # place the legend in the bottom right corner, a.k.a location 4
michael_scott.axhline(0, color="black", linestyle = "--") # add in the horizontal origin line because I like having it
michael_scott.axvline(0, color="black", linestyle = "--") # add in the vertical origin line because I like having it

pyplot.show() # show off the plot to the world