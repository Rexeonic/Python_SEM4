# initializing how many people are there 10 or (binary 1 or 0 )
types_of_people = 10
# make use of 10 as there are 2 types of people (if you know binary) 
x = f"There are {types_of_people} types of people."

# initializing binary string
binary = "binary"
# initializing don't string
do_not = "don't"
# string formating using above 2 string variables
y = f"Those who know {binary} and those who {do_not}"       # string is putted inside string

# printing of x and y
print(x)
print(y)

# Actual Joke statement
print(f"I said: {x}")                           # string is putted inside string
print(f"I also said: '{y}' ")                   # string is putted inside string

# was it hilarious (storing that info)
hilarious = False
# printing the result of the joke, whether it was hilarious or not
joke_evaluation = "Isn't that joke so funny?!  {} {} \n\t\t\t\t\t{}"         # string is putted in string in next instruction (more precisely a boolean)

# using .format syntax to do formatting to already initialized string
print(joke_evaluation.format(x,y, hilarious)) #(joke_evaluation.format(hilarious))

# some more statements
w = "This is the left side of..."
e = "a string with a right side."

# Concatenating and then printing the above 2 statements
print( w + e )