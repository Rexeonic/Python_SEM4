name = 'Zed A. Shaw'
age = 35 

# Height 
height = 74 # inches
height_ft = height / 12
height_cm = 74 * 2.54

print(f"Height {height_cm} cms")
print("")

# Weight
weight = 180 # lbs
weight_kg = weight * 0.4536


eyes = 'Blue'
teeth = 'White'
hair = 'Brown'


print(f"Let's talk about {name}")
print(f"He's {height} inches/{round(height_ft)} ft/ {height_cm} cms tall")
print(f"He's {weight} lbs/{weight_kg} kgs heavy")
print(f"Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + weight + height
print(f"If I add {age}, {height}, and {weight} I get {total}")