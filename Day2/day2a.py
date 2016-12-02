# Open file
f = open("A.txt")

lines = f.readlines()

# Keypad
keypad = [1, 2, 3,
          4, 5, 6,
          7, 8, 9]
current = 4


# Make sure it doesn't end up pass the array
def safeSubtract(current, val):
    invalid = [2, 5]
    if (((current - val) not in invalid) or val != 1) and (current - val) >= 0:
        current -= val
    return current


def safeAdd(current, val):
    invalid = [3, 6]
    if (((current + val) not in invalid) or val != 1) and (current + val) < len(keypad):
        current += val
    return current


# Go through each line
for line in lines:
    # Go through each instruction
    for char in line:
        if char == "U":
            current = safeSubtract(current, 3)
        elif char == "D":
            current = safeAdd(current, 3)
        elif char == "L":
            current = safeSubtract(current, 1)
        elif char == "R":
            current = safeAdd(current, 1)
    # Print the code each time, no end so keeps the digits together
    print(current + 1, end="")
