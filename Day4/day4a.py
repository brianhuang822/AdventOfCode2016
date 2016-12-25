import operator

# Open file
f = open("A.txt")
# Put our data parsed into an array
lines = f.readlines()

# Current sum of ids
total = 0

for line in lines:
    # Strip the whitespace and new line chracters
    line = line.strip()
    # The encrypted name is on the left side of the last index
    encrypted_name = line[:line.rindex("-")]
    # The sum and order are on the right side of the index
    # Splitting it by '[' gets the sum on the left and order on the right assignment
    current_sum, order = line[line.rindex("-") + 1:].split("[")
    # strips the ']' from order order list
    order = order[:-1]

    current_dict = {}
    for character in encrypted_name:
        # Ignore the dash and count the number of each character in our name
        if character == '-':
            pass
        elif character in current_dict:
            current_dict[character] += 1
        else:
            current_dict[character] = 1

    # Covert our dictionary to tuples to make it easier to multi-level sort
    tuple_list = []
    for key in current_dict:
        tuple_list.append((key, current_dict[key]))

    # Now sort the tuple_list by value (1), then key (0)
    # We're allowed to do this since Python sorting is stable (sorting a 2nd time won't mess with the ordering of 1st)
    # We just need to sort by the secondary key first (letter) then our primary (numerical)
    tuple_list = sorted(tuple_list, key=operator.itemgetter(0), reverse=False)
    tuple_list = sorted(tuple_list, key=operator.itemgetter(1), reverse=True)

    # Check if our checksum is valid, going through each letter
    matching = True
    for i in range(len(order)):
        # If our checksum list isn't the same as our ordered list, then it's not a valid room
        if order[i] != tuple_list[i][0]:
            matching = False

    # If all letters passed, add our current_sum with our total
    if matching:
        total += int(current_sum)

# After going through all the rooms, output the total
print(total)
