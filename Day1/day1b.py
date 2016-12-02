# Open file
f = open("A.txt")
# Put our data parsed into an array
data = f.readlines()[0].replace(" ", "").split(",")

# Starting location
x = 0
y = 0
currentDirection = 0

# Keep track of locations visited
visited = []


def checkCurrent():
    # check if visited
    global visited
    global x
    global y
    if (x, y) in visited:
        print(abs(x) + abs(y))
        exit(0)
    else:
        visited.append((x, y))


for instruction in data:
    # Turning left or right
    currentDirection = (currentDirection - 1) if instruction[0] == 'L' else (currentDirection + 1)
    # If it's 0, 1, its N or E in NESW
    distance = int(instruction[1:])
    for i in range(distance):
        # If it's 0, 1, its N or E in NESW
        if currentDirection % 4 == 0 or currentDirection % 4 == 1:
            # If its 0, its N or S in NESW
            if currentDirection % 2 == 0:
                # parse number and add
                x += 1
            else:
                y += 1
        else:
            if currentDirection % 2 == 0:
                x -= 1
            else:
                y -= 1
        # Check if intersect at each step
        checkCurrent()
