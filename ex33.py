#                                   LOOPS FILE

i = 0               # parameter variable
offset = 1          # determines the offset with which number is increment in while_loop
numbers = []        #  creates empty list
limit = 6           # how much time the while loop function is called


# -----------------------------------------------------------------------------------------

# range function
# upper limit isn't included
# range (start, stop, step)  i.e range(i, j)
# return an list = [i, i+1, i+2,....., j-1]

# implementation of range
def my_range(start, stop, step = 1, index = 0):    # step = 1 is the default value otherwise usersupplied value
        value = start               # just for better functioning, can remove if you like
        if value < stop:
            value += step

            list1 = [value, my_range(value, stop, step, index = index + 1)]
            
            if value == stop:
                return value
        else:
             return
        
        #return [item for sublist in list for item in sublist]
        return list(flatten(list1))

# -----------------------------------------------------------------------------------------

# do-while runs the block ones
# then checks for given statement is true or false
def do_while_loop(x, incremental_size):

    ''' JMD created do_while-loop (for implementation purposes.)
            abbr*
                DNR --> Do not remove [Fatal]
    '''
    print(f"At the top i is {x}")
    numbers.append(x)

    x += incremental_size
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {x}")

    if x < limit:           # DNR
        while_loop(x, incremental_size)
    
# while loop
# while loop keeps running until the statement becomes false
def while_loop(x, incremental_size):
        
        ''' JMD created while-loop (for implementation purposes.)
            abbr*
                DNR --> Do not remove [Fatal]
        '''
        if x < limit:
            print(f"At the top i is {x}")
            numbers.append(x)

            x += incremental_size
            print("Numbers now: ", numbers)
            print(f"At the bottom i is {x}")
        
            while_loop(x, incremental_size)         # DNR

        else:
            exit

# for loops
# for loops checks the condition, runs, and increment counter
def for_loop(x, incremental_size):
    
    ''' JMD created for-loop (for implementation purposes.)
        abbr*
            DNR --> Do not remove [Fatal]
    '''
    
    if (x < limit):
        # LOOP code could be replaced accordingly
        print(f"At the top i is {x}")
        numbers.append(x)

        x += incremental_size
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {x}")

        for_loop(x, incremental_size)            # DNR
    else:
        exit


#while_loop(i, offset)          # testing done (results verified)
#do_while_loop(i, offset)       # testing done (results verified)
for_loop(i, offset)             # testing done (results verified)

#while i < 6:
#    print(f"At the top i is {i}")
#    numbers.append(i)

#    i = i + 1
#    print("Numbers now: ", numbers)
#    print(f"At the bottom i is {i}")
#

print("The numbers: ")

for num in numbers:
    print(num)

list1 = my_range(0, 6, 1)
print(list1)