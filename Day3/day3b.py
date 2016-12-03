# Open file
f = open("A.txt")
# Put our data parsed into an array
lines = f.readlines()
# Num of valid triangles
valid = 0
# All our values, we'll later transform the data to something we know how to solve
preTransform = []
for line in lines:
    # Split the string
    lineSplit = line.split(" ")
    values = []
    for string in lineSplit:
        # Get the non empty strings (our numbers) and store it
        if string.strip() != "":
            values.append(int(string.strip()))
    preTransform.append(values)

postTransform = []
# Count by 3s
for i in range(0, len(preTransform), 3):
    # Add vertically down to our postTransform
    for j in range(3):
        postTransform.append([preTransform[i][j], preTransform[i + 1][j], preTransform[i + 2][j]])

for values in postTransform:
    # Sort smallest to largest
    values.sort()
    # If valid triangle, increment
    if values[2] < values[1] + values[0]:
        valid += 1
print(valid)
