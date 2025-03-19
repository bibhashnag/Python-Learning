# Testing output to the console.

# messages variables
message1 = "I am new to Python"
message2 = "I am here to learn"
message3 = "Thank you for your love and support"
message4 = "Have a nice day."

# Basic use, print(Any_message)
print("Hello World!")

# Sending multiple messages
print(message1, message2, message3)

# Sending multiple messages with a separator
print(message1, message2, message3, sep=".")

# By default after the print, the control goes to the next line
# We can change that by end parameter
print(message1, message2, message3, sep=".", end=".")
print(message4)

