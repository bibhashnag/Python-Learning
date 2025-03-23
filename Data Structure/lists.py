# List is a sequence of value of any type
# It is mutable i.e. you can add, remove and edit the value in a list
# It has a numeric index starting with 0

States_in_India = ["Odisha", "Telengana", "Maharastra", "Punjab", "Haryana", "Andhra Pradesh"]

States_in_India.append("Tamilnadu")
States_in_India.append("Himachal")
States_in_India.insert(3, "Goa")

# States_in_India.pop(2)
# States_in_India.remove("Haryana")

# # print(States_in_India)
# count = 1
# for state in States_in_India:
#     print(f"State No. {count}: {state}")
#     count += 1

# Before Sorting
# print("Befor Sorting")
# print(States_in_India)

# print("After Sorting...")
# States_in_India.sort()
# print(States_in_India)


# slicing a list
print(States_in_India[3:])
