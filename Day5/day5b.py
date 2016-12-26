import hashlib

# Open file
f = open("A.txt")
# First line is our input
puzzle = f.readline()
# Current number
current = 0
# current pass, set to - if unseen
current_pass = "--------"


# helper function to check if all filled
def isfilled(current):
    for char in current:
        if char == "-":
            return False
    return True


# keep going until we have all 8
while not isfilled(current_pass):
    # hash with library
    current_hash = hashlib.md5((puzzle + str(current)).encode('utf-8')).hexdigest()
    # check if chracter has 5 0s
    # will try on convert to int so may crash
    try:
        index = int(current_hash[5])
        if current_hash[:5] == "00000" and index < 8 and current_pass[index] == "-":
            # Replace the position with the number we want
            current_pass = current_pass[:index] + current_hash[6] + current_pass[index + 1:]
            print(current_pass)
    except:
        pass

    # add one to current to check our next one
    current += 1
print(current_pass)
