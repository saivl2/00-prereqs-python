text = input().lower().split()

counter = 0
for word in text:
    if word == 'emma':
        counter += 1
print(counter)