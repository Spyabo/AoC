txt = open("/home/spy/AoC2022/Day6/input.txt", "r")
datastream = txt.read()

for i in range(len(datastream) - 3):
    # Get the four characters at the current position
    chars = datastream[i:i+4]

    # Check if the four characters are all different
    if len(set(chars)) == 4:
        # If they are, then this is the start of the packet
        print(i+4) # Add 4 to account for 0-indexing
        break