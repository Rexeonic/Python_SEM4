# Using format function to turn the formatter variable into other strings


# empty string is initialized with parentheses for post-string formating
formatter = "{} {} {} {}"

# post string formating
print(formatter.format(1, 2, 3, 4))
print(formatter.format("Monday", "Tuesday", "Wednesday", "Thurday"))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, True, False))

# string is getting formatted by the string itself
print(formatter.format(formatter.format(formatter, formatter, formatter, formatter.format(1,2,3,4)), formatter, formatter, formatter))

# A Poem
print(formatter.format(
        "kapi sen sang sanghari nischar ram sitahi aanihe",
        "\ntrelok pavan sujasu sur muni naradadi bakhanihe",
        "\no sunat gavat samujhat param pad nar pavaee",
        "\nraghubir pad pathoj madhukar das tulsi gavaee"
))


#   Points to note
#   1. string inside .format() should be done as of any string (i.e inside "")
#   2. True, False are boolean if not inside string (if want them to be string put inside "")
#   3. else everything can be without ""
#
#