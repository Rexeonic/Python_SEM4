# Mary's poem getting printed
print("Mary had a little lamb.")
print(5 * "Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10)     # what'd that do?   . gets printed 10 times

# Each alphabet of cheese burger is getting stored
#end1 = "C{}{}{}{}{}{}{}{}{}{}{}{}"
end1 = "C"
end2 = "h"
end3 = "e"
#end4 = "e"
end5 = "s"
#end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
#end11 = "e"
end12 = "r"

# watch end = ' ' at the end. Remove it to see what happens
# (on removing end = ' ' ) Burger gets written to the next line
print(end1 + end2 + end3 + end3 + end5 + end3, end=' ')
print(end7 + end8 + end9 + end10 + end3 + end9)
#print(end1.format(end2 , end3 , end4 , end5 , end6,' ' , end7 , end8 , end9 , end10 , end11 , end12))