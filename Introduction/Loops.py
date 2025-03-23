# # While loop 
# count = 0
# while count <= 20:
#     print("*" * count)
#     count+=1

# # For loop
# fruits = ["apple", "banana", "cherry", "date"]

# for fruit in fruits:
#     print(fruit)

# for number in range(10, 100, 10):
#     print(number)
#     number += number + 10

# Changing the natural flow of loop

for number in range(10, 100, 10):
    if number > 50:
        break
    else:
        print(number)
        number += number + 10
        continue