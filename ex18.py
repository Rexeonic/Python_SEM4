#   Functions

# this one is like your scripts with argv
def print_two(*args):                       # argument packing during function call
    arg1, arg2 = args                       # argument unpacking
    print(f"arg1: {arg1}, arg2: {arg2}")    # function logic

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one Argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Zed", "Shaw")
print_two_again("Angerston", "Buckley")
print_one("Bethesda")
print_none()



#                       FUNCTION CHECKLIST
#   Checklist 1
#1. Did you start your function definition with def
#2. Does your function name have only characters and _ characters?
#3. Did you put an open parenthesis right after the function name?
#4. Did you put your arguments after the parenthesis separated by commas?
#5. Did you make each argument unique (meaning no duplicated names)?
#6. Did you put a close parenthesis and a colon after the arguments?
#7. Did you indent all lines of code you want in the function four spaces? No more, no less.
#8. id you "end" your function by going back to writing wit h no indent (dedenting, we call it)?
#
#   Checklist 2
#           When you run ("use" or "call") a function, check thiese thing:
#
#1. Did you call/use/run this function by typing its name?
#2. Did you put the (character after the name to run it)?
#3. Did you put the values you want into the parenthesis separated by commas?
#4. Did you end the function call with a ) character?
