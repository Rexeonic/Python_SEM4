# variable are being assigned string
tabby_cat = "\tI'm tabbed in."          # escape sequences are modifying strings
persian_cat = "{}I'm split\non a line."   # like HTML
backslash_cat = "I'm \\ a \\ cat."

# \b ( one backspace )  \t ( one tab or 8 spaces )
fat_cat = """
{}I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# All the variables are getting printed
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# Homework
print(fat_cat.format(backslash_cat) , "\n" , "\N{0x10FFFF}" , persian_cat.format(tabby_cat))      # Turn into however complex you'd want to
