from sys import argv
from os.path import exists

script, from_file, to_file = argv   # from_file, to_file are string (name of files)

#print(f"Copying from {from_file} to {to_file}")

# We could do these two on one line, how?
#in_file = open(from_file)
#indata = in_file.read()
indata = open(from_file).read()         # reads file and closes when statement's processed

#print(f"The input file is {len(indata)} bytes long")

#print(f"Does the output file exist? {exists(to_file)}")
print(f"Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)
#out_file.write(str(in_file.read()))    # doesn't work

print("Alright, all done.")

out_file.close()
#in_file.close()        # not necessary , read the program with comments