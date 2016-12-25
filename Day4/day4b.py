import operator

# Open file
f = open("A.txt")
# Put our data parsed into an array
lines = f.readlines()

# The id to find
sector_id = 0

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
    # current_sum to int
    current_sum = int(current_sum)

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

    # Ignore the invalid room
    if matching:
        actualName = ""
        # Go through every character and decipher
        for letter in encrypted_name:
            # Dash becomes blank
            if letter == '-':
                actualName += " "
            else:
                # ascii a starts at 97, so subtracting 97 becomes 0
                # We can then add the shift amount and mod it by 26 (# of letters of alphabet)
                # such that when it goes to 26+, it modulo back down to 0-25
                # Finally, add 97 back to get to ascii letters and change it back to char
                actualName += chr((ord(letter) - 97 + current_sum) % 26 + 97)
        # For fun, here's the decoded names
        print(actualName)
        # Find the sector id
        if "north" in actualName and "pole" in actualName and "object" in actualName:
            sector_id = current_sum

print(sector_id)
