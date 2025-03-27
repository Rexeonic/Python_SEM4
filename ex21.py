from math import pi

def add(a, b):
    print(f"Adding: {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting: {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying: {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Divinding: {a} / {b}")
    return a / b

print("Let's do some math with just functions")

age = add(30, 5)
height = subtract(78, 9)
weight = multiply(pi, 2)
iq = divide(100, 2)

# A puzzle for the extra credit, type it in anyway
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")
#print("Age: {}, Height: {}, Weight: {}, IQ: {}".format(age, height, weight, iq))

# Expression, what = age + [ height - { weight * (iq/2) } ]
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# Expression, what = height * weight / age + iq
now = add(divide( multiply(height, weight), age ), iq)

print("That becomes: ", what, now, "Can you do it by hand?")