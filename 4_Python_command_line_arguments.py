#python command line arguments

import sys


# len() is an inbuilt function of Python which can be used to find the length of any iterable data type
# Command line arguments are run through cmd

n = len(sys.argv)

command_line_args = sys.argv

print("Total number of command line arguments :", n)
print("What are the different command line arguments? ", command_line_args)

print("The first command ine argument :" , sys.argv[0])
print("The second command ine argument :" , sys.argv[1])
print("The third command ine argument :" , sys.argv[2])
print("The fourth command ine argument :" , sys.argv[3])