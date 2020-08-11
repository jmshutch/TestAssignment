#---------------------------------------------------------------------------------
# Name:        Exercise03.py
# Purpose:     convert geographic coordinates in DDMMSS format to DD (using input)
# Author:      shutch
# Created:     09/11/2019
#---------------------------------------------------------------------------------

# accept user-defined input coordinates in the specific DDMMSS format as string
x = input("Please enter a coordinate value in DDMMSS format: ")

# slice the input string to isolate the last two values (SS), convert,
# convert to integer, and divide by 60 to compute minutes equivalent
ss = int(x[4:]) / 60.0

# slice the input string to isolate the last the middle two values (MM),
# convert to integer, add SS in their MM equivalents and divide by 60
# to compute DD equivalent
mm = (int(x[2:4]) + ss) / 60.0

# slice the input string to isolate the first two values (DD), convert
# to integer, and add MM in their DD equivalent
dd = int(x[0:2]) + mm

# print the result and round the solution to two decimal places
print "The solution in decimal degrees is:", round(dd, 2)

# I added this new comment.

