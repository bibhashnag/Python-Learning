# Trying out different types of variables.

# name = value
# values can be literal, another variable, or the result of an operation or function call

book_name = "AI for Managers"
number_of_pages = 400
price = 39.99
tax = price * 0.10

name = input("Hi! Please enter your name:")
print(f'Hi {name}, thank you for purchasing the book {book_name}')
print(f'It has a total of {number_of_pages} pages')
print(f'The price of the book is: {price}')
print(f'Tax will be: {tax}')