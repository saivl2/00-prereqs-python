# Sets accepts unique items and have no order

art_friends = {'Rolf', 'Anne'}
science_friends = {'Jen', 'Charlie'}
art_friends.add('Jen')
print(type(art_friends))
print(art_friends)

# art_friends.remove('Jen')

print({1,1,1,2,3,4,4,4,5})

# Set operations
print(art_friends)
print(science_friends)

art_but_not_science = art_friends.difference(science_friends)
print(art_but_not_science)


not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)

art_and_science = art_friends.intersection(science_friends)
print(art_and_science)

all_students = art_friends.union(science_friends)
print(all_students)