import hashlib

# Open file
f = open("A.txt")
# First line is our input
puzzle = f.readline()
# Current number
current = 0
# current pass
current_pass = ""
# keep going until we have all 8
while len(current_pass) < 8:
    # hash with library
    current_hash = hashlib.md5((puzzle + str(current)).encode('utf-8')).hexdigest()
    # check if chracter has 5 0s
    if current_hash[:5] == "00000":
        current_pass += current_hash[5]
    # add one to current to check our next one
    current += 1
print(current_pass)
