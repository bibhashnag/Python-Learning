class Friends:
    def __init__(self, name, city, likes):
        self.name = name
        self.city = city
        self.likes = likes
        self.friends_list = []
        self.friends_list.append(name)
        self.friends_list.append(city)
        self.friends_list.append(likes)

    def add_friend(self, name, city, likes):
        if name not in self.friends_list:
            self.friends_list.append(name)
            self.friends_list.append(city)
            self.friends_list.append(likes)
            return f"{name} has been added to your friends list."
        else:
            return f"{name} is already in your friends list."

    def remove_friend(self, name):
        if name in self.friends_list:
            self.friends_list.remove(name)
            return f"{name} has been removed from your friends list."
        else:
            return f"{name} is not in your friends list."

    def get_friends(self):
        return self.friends_list
    

# Example usage:
my_friends = Friends("Alice", "New York", ["music", "travel"])
print(my_friends.add_friend("Bob", "Los Angeles", ["sports", "movies"]))
print(my_friends.get_friends())



