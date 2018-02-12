# Homework #2 for Physics 165 by Isaac Pliskin
# Working with inputting and outputting files
# The data file is data1.txt
# output files should be Mult_2.txt and Sqrt_Col2.txt
from numpy import array, sqrt 

# Begin question 1
data_points = [[], []] # two dimensional list to hold both columns of data
with open("data1.txt", "r") as file: # opens the file
    for line in file:
        data = line.split()
        data_points[0].append(float(data[0]))
        data_points[1].append(float(data[1]))

column_one = array(data_points[0])
column_two = array(data_points[1])

column_one = column_one * 2
column_two = sqrt(column_two)

print("First array is: ", column_one)
print("Second array is: ", column_two)

with open("Mult_2.txt", "w") as output:
    for item in column_one:
        output.write("{}\n".format(item))
    print("First array saved as Mult_2.txt")

with open("Sqrt_Col2.txt", "w") as output:
    for item in column_two:
        output.write("{}\n".format(item))
    print("Second array saved as Sqrt_Col2.txt")