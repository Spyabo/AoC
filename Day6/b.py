txt = open("/home/spy/AoC2022/Day6/input.txt", "r")
datastream = txt.read()

# Loop over the characters in the datastream, 14 at a time
for i in range(len(datastream) - 13):
    # Get the 14 characters at the current position
    chars = datastream[i:i+14]

    # Check if the 14 characters are all different
    if len(set(chars)) == 14:
        # If they are, then this is the start of the message
        print(i+14) # Add 14 to account for 0-indexing
        break