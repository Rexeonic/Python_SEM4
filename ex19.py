#   function definition
#def cheese_and_crackers(cheese_count, boxes_of_crackers):
#    print(f"You have {cheese_count} cheeses!")
#    print(f"YOu have {boxes_of_crackers} boxes of crackers!")
#    print("Man that's enough for a party!")
#    print("Get a blanket.\n")

# Calling function and passing arguments directly
#print("We can just give the function numbers directly:")
#cheese_and_crackers(20, 30)

# Calling function and passing variables
#print("OR, we can use variables from our script:")
#amount_of_cheese = 10
#amount_of_crackers = 50

#cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Calling function and passing arithmetic expression
#print("we can even do math inside too:")
#cheese_and_crackers(10 + 20, 5 + 6)

# Calling function and passing arithmetic expression (both literals and Identifiers)
#print("And we can combine the two, variables and math:")
#cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def my_function(fname):
    print(fname + "Reference")

my_function("Tobias")

def function1(fname, lname):
    print(fname + " " + lname)

function1("Email", "Refsnes")

def function2(*kids):
    print("The youngest child is " + kids[2])

function2("Email", "Tobias", "Linus")

def function3(child3, child2, child1):
    print("The youngest child is " + child3)

function3(child1 = "Lily", child2 = "Tobias", child3 = "Linus")

def function4(**kids):                              # don't know how many arguments
    print("His last name is " + kids["lname"])       # **kids (dictionary of arguments)

function4(fname = "Tobias", lname = "Refsnes")

def function5(country = "Norway"):                  # function with default argument
    print("I am from" + country)

function5("India")
function5()

def function6(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
function6(fruits)


def function7(x):
    return 6*x
print(function7(9))

def function8():    # function def cann't be empty
    pass

# Position only arguments  i.e function(3)
# e.g
def func(x, /):
    print(x)

func(3)     # func( x = 3 ) will produce error

# keyword only arguments   i.e function( x = 3)
def func2(*, x):
    print(x)

func2( x = 3 )      # func(3) will produce error

def function9(a, b, /, *, c, d):
    print(a + b + c + d)

function9(5, 6, c = 7, d = 8)


#
#
#       Function Recursion

def tri_recursion(k):   # if k>0 then 1 else 0 will get returned
    if(k > 0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
        return result

print("Recursion Example Results:")
tri_recursion(6)