#  argv is a List of input strings
from sys import argv
#  read the WYSS section for how to run this
#script, first, second, third = argv


#   Perform same function
#print("The script is called:", script)
#print("Your first variable is:", first)
#print("Your second variable is:", second)
#print("Your third variable is:", third)
print("The script is called:", argv[0])
print("Your first variable is:", argv[1])
print("Your second variable is:", argv[2])
print("Your third variable is:", argv[3])


print("let's print some more!!")

#print("Your fourth variable is:", end = ' ')
fourth = input("Your fourth variable is: ")

print("Input becomes: {} {} {} {}".format(argv[1], argv[2], argv[3], fourth))
#   if less argv are given, then
#   all the variables aren't assigned values
#   null variables cann't be implemented (as generates error)