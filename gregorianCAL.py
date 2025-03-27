#  This program calculates from a fixed point in calendar date.

# def
#   fixed-from-gregorian (year|month|day)  =       
#                       
#                       gregorian-epoch - 1 * 365 * (year - 1) + [ (year - 1) / 4 ] - [ (year - 1) / 100 ]
#
#                       + [ (year - 1) / 400 ] + [ ( 1  /  12) * ( ( 367 * month ) - 362 ) ] + f(x) + day

#   f(x) = { 0      if month <= 2
#           -1    if gregorian-leap-year? (year)
#           -2      otherwise
#          }


# example QUESTION
# Acc. to Gregorian Calendar, it was Monday on the date 01/01/01. If any year is input through the keyboard
# Write a program to find out what is the day on 1st January of this year

# Currently works for future years
# Input the year
year = int(input("Enter the year excluding century:"))                            #input["Enter the year:"]

# Calculate whether entered year is leap year
# rem_4 = year % 4
# rem_100 = year % 100
# rem_400 = year % 400

# if( (rem_4 == 0) | ( rem_100 == 0 & rem_400 == 0 ) ):
#    leapyear = -1       # as it is a leapyear
# else:
#    leapyear = 0
#

# Shorting the formula
totaldays = 365 * (year - 1 ) + ((year-1)/4) - ((year-1)/100) + ((year-1)/400)

day = totaldays % 7
day = round(day)

if( day == 0):
    print("It is Monday")


if( day == 1):
    print("It is Tuesday")
    
if( day == 2):
    print("It is Wednesday")
    
if( day == 3):
    print("It is Thursday")
    
if( day == 4):
    print("It is Friday")
    
if( day == 5):
    print("It is Saturday")

if( day == 6):
    print("It is Sunday")