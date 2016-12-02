# Open file
f = open("A.txt")
# Put our data parsed into an array
data = f.readlines()[0].replace(" ", "").split(",")


#Starting location
x = 0
y = 0
currentDirection = 0

for instruction in data:
    #Turning left or right
    currentDirection = (currentDirection - 1) if instruction[0] == 'L' else (currentDirection + 1)
    #If it's 0, 1, its N or E in NESW
    if currentDirection % 4 == 0 or currentDirection % 4 == 1:
        #If its 0, its N or S in NESW
        if currentDirection % 2 == 0:
            #parse number and add
            x += int(instruction[1:])
        else:
            y += int(instruction[1:])
    else:
        if currentDirection % 2 == 0:
            x -= int(instruction[1:])
        else:
            y -= int(instruction[1:])
print (abs(x) + abs(y))