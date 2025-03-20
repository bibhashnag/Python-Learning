# Practicing String manipulation

# Single line text output using single quote
print('Using single quotes to display this message')

# Single line text output using double quotes
print("Now using double quotes to display this message")

# Multi line text output using three single quotes
print('''This is multi line message. 
      Using single quotes for this.
'''
)

# Multi line text output using three double quotes
print("""This is multi line message. 
      Using single quotes for this.
"""
)

# Escapting quotes with in a string by using double quotes
print("What's the next topic to learn?")

# Escapting quotes with in a string by using escape character
print('What\'s the next topic to learn?')

# Concatenating two strings. 
message1 = "This is the first string"
message2 = "This is the second string"

print(message1, message2, sep=".")

# Calculating the length of the message
message3 = "The quick brown fox jumped out of the bush"

print(f"The length of the string \"{message3}\" is:", len(message3))

# Repetation of a string
print("*" * 20)
print("/" * 20)
print("-" * 20)
print("/\\" * 20)

# Playing with Upper case, Lower case and Title
message4 = "converting from lower to upper case"
message5 = "CONVERTING FROM UPPER TO LOWER"
message6 = "converting the first letter of every word to upper case"

print(message4.upper())
print(message5.lower())
print(message6.title())

# message trimming
message7 = "       Python Programming       "

print(message7)
print(message7.strip())
print(message7.rstrip())
print(message7.lstrip())

# Replace operation with string
message8 = "I like Movies. Movies are fun. Comedy Movies are my favorite."

print("Replacing the word Movies with Theater")
print(message8.replace("Movies", "Theater"))

# find operation with String
print("The word Movies found at index:", message8.find("Movies"))

# count operation with string
print(f"The count of word \"Movies\" in the string \"{message8}\" is:", message8.count("Movies"))

# Retrieving the character of a particular index from the beginning of a string
print(message8[0])
print(message8[1])
print(message8[2])

# Retrieving the character of a particular index from the end of a string
print(message8[-1])
print(message8[-2])
print(message8[-3])