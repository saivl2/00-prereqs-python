data = map(int, input().split())

def check_duplicate(l):
    unique = []
    for item in l:
        if item not in unique:
            unique.append(item)
    return unique

print(check_duplicate(data))