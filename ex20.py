from sys import argv

# Unpacking of the argv (list)
script, input_file = argv

# prints the whole file
def print_all(f):
    print(f.read())

# Takes the cursor/pointer to the index of the file
def rewind(f):
    f.seek(0)

# Prints a specific given line
def print_a_line(line_count, f):
    print("Line Number:", line_count)
    print(line_count, f.readline())

# Opens the file given by user
current_file = open(input_file)

print("First let's print the whole file:\n")

# calling print_all function
print_all(current_file)

print("Now let's rewind, kind of like a tape")

# calling rewind function (taking cursor at index)
rewind(current_file)

print("Let's print three lines:")

# Printing the first line
current_line = 1
print_a_line(current_line, current_file)

# Printing the 2 line and consecutive lines in the next statements
current_line += 1
print_a_line(current_line, current_file)

# Printing the 3rd line
current_line += 1
print_a_line(current_line, current_file)

# Printing the 4th line
current_line += 1 
print_a_line(current_line, current_file)

# Printing the 5th line
current_line = current_line + 1
print_a_line(current_line, current_file)        # prints the line 5