l1 = list(map(int, input().split(',')))
l2 = list(map(int, input().split(',')))

new_list = []

for n1 in l1:
    if n1 % 2 != 0:
        new_list.append(n1)
for n2 in l2:
    if n2 % 2 == 0:
        new_list.append(n2)

print(new_list)