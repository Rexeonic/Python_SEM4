from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit Ctrl-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file....")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
#target.write(f"{line1} \n {line2} \n {line3}")

target.write("{}\n{}\n{}\n".format(line1, line2, line3))

print("And finally, we close it.")
target.close()


# Study Drill   (to read ex16_file.txt)
#
# from sys import argv
# 
# script, filename = argv
# file = open(filename)
#                           # or 
# #filename = input("Open the file: \n > ")
# #file = open(filename)
# 
# print(file.read())
#    
# print("Ctrl-C to exit, press RETURN to continue")
#
# print("Type the filename: \n > ")
# 
#
#