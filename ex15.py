#from sys import argv

# Use Notes, Mistakes or Topic file as argument(filename) while running the script
#script, filename = argv

filename = input("Type the filename to open\n > ")
# filename is opened and returned parameters are stores into txt variable
txt = open(filename)            # txt is <class '_io.TextIOWrapper'>

# formatted string is printed using variable filename { or argv[1] }
print(f"Here's your file {filename}:")  
print(txt.read())               # file is read and that data is printed
txt.close()                     # It is Important to close files

# Prompting user to make what type of input
#print("Type the filename again:")
#file_again = input("> ")        # input is takes and stored into file_again
#
#txt_again = open(file_again)    # file is opened
#
#print(txt_again.read())         # file is read nad that data is printed
#txt_again.close()


