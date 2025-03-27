from sys import argv
import codecs

script, filename = argv

def encrypt(data, error):
    code = codecs.encode(str.encode(data), encoding = "base64", errors = error)
    file = open(filename, 'w')
    file.write(str(code))
    file.close()

#   NOT Completed
def decrypt(data, error):
    #codec = input("Enter Key: (Hint: Encoding name)\n> ").strip()
   
    text = codecs.decode(str.encode(data), encoding = "base64", errors = error)
    file = open(filename, 'a')
    file.write(str(text))
    file.close()

print("Type Errors:\n\tstrict (preferred) \n\treplace (if error encountered)")
error = input("> ").strip()

Choice = int(input("Select \n\t 1. Encrypt \n\t 2. Decrpyt \n > "))

file = open(filename, 'r+')
data = file.read()
file.close()

if Choice == 1:
    encrypt(data, error)
if Choice == 2:
    data = data.strip('b')
    data = data.strip('\'')
    decrypt(data, error)