people = 30
cars = 40
trucks = 15

# Check if Cars are more than people
if cars > people:
    print("We should take the cars.")
elif cars < people:     # Checks if cars are less than people
    print("We should not take the cars.")
else:                   # If not the above then print this
    print("We can't decide.")

if trucks > cars:       # If trucks are greater than cars
    print("That's too many trucks.")
elif trucks < cars:     # If trucks are less than cars
    print("Maybe we could take the trucks.")
else:                   # If not the above then print this
    print("We still can't decide.")

if people > trucks:     # Checks if people are greater than trucks
    print("Alright, let's just take the trucks.")
else:                   # If not the above
    print("Fine, let's stay home then.") 