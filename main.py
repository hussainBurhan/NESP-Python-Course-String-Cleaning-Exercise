# Initializing a string variable 'name'
name = 'coding4startups'

# Initializing a counter variable 'i'
i = 0

# Using a while loop to iterate through the characters of 'name'
while i < len(name):
    # Checking if the character at index 'i' is '4'
    if name[i] == '4':
        # If '4' is found, increment 'i' and continue with the next iteration
        i += 1
        continue
    # If character is not '4', print it without a newline
    print(name[i], end="")
    # Increment 'i' for the next iteration
    i += 1

    