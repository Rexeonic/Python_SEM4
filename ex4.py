# Defines number of space in a car
cars = 100

# Defines passenger capacity
space_in_a_car = 4.0

# Defines drivers available to drive 
drivers = 30

# Number of passengers
passengers = 90

# Cars which aren't being drived
cars_not_driven = cars - drivers

# Car which are being driven
cars_driven = drivers

# Passengers that can be taken (into cars being drived)
carpool_capacity = cars_driven * space_in_a_car

# Avg number of passengers per car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")