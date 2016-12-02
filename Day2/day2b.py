# Open file
f = open("A.txt")

lines = f.readlines()

# Keypad
keypad = [-1, -1, 1, -1, -1,
          -1, 2, 3, 4, -1,
          5, 6, 7, 8, 9,
          -1, "A", "B", "C", -1,
          -1, -1, "D", -1, -1]
current = 10


# Make sure it doesn't end up pass the array
def safeSubtract(current, val):
    invalid = [10]
    if (((current - val) not in invalid) or val != 1) and (current - val) >= 0 and keypad[current - val] != -1:
        current -= val
    return current


def safeAdd(current, val):
    invalid = [15]
    if (((current + val) not in invalid) or val != 1) and (current + val) < len(keypad) and keypad[current + val] != -1:
        current += val
    return current


# Go through each line
for line in lines:
    # Go through each instruction
    for char in line:
        if char == "U":
            current = safeSubtract(current, 5)
        elif char == "D":
            current = safeAdd(current, 5)
        elif char == "L":
            current = safeSubtract(current, 1)
        elif char == "R":
            current = safeAdd(current, 1)
    # Print the code each time, no end so keeps the digits together
    print(keypad[current], end="")
