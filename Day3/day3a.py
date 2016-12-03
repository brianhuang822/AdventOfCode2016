# Open file
f = open("A.txt")
# Put our data parsed into an array
lines = f.readlines()
# Num of valid triangles
valid = 0
for line in lines:
    # Split the string
    lineSplit = line.split(" ")
    values = []
    for string in lineSplit:
        # Get the non empty strings (our numbers) and store it
        if string.strip() != "":
            values.append(int(string.strip()))
    # Sort smallest to largest
    values.sort()
    # If valid triangle, increment
    if values[2] < values[1] + values[0]:
        valid += 1
print(valid)
