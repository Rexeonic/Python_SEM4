# Improved ex17.py Script   # A four line copy file code
from sys import argv

from_file, to_file = argv[1:]

indata = open(from_file).read()
open(to_file, 'w').write(indata)