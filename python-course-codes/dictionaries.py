friend_ages = {
    'Rolf': 24, 
    'Adam': 30, 
    'Anne': 23
}

# Get the value
print(friend_ages['Anne'])
print(friend_ages.get('Ron', 0)) # if the key ddoes not exist it defaults to 0

# Changing values

friend_ages['Rolf'] += 3
print(friend_ages)

# Nested dictionaries
friends = {
    'friend1': {'name': 'Adam', 'age': 34},
    'friend2': {'name': 'Ron', 'age': 45}
}
print(friends['friend1']['name'])  # Access: Adam

friends = [
    ('Rolf', 45), 
    ('Adam', 40),
    ('Anne', 34)
]

print(dict(friends))