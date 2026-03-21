friends = ['Amy', 'Bob', 'Ron']
random_list = [True, 4.5, "Hello"]

print(friends[2])
print(random_list[-1])

MyList = [['apple', 'banana', 'cherry'], [22, 14, 16], [True, False, True]]

print(MyList[2][2])

# Addding items to list
friends.append('Henry')

# Removing items from list
MyList.remove(['apple', 'banana', 'cherry']) # Value you will remove

# Chaning items in lists - mutable
friends[3] = "Bobby"
print(friends)

# Joining lists
l1 = ['a', 'b', 'c', 'd']
comma_seperated = ' '.join(l1)

print(comma_seperated)