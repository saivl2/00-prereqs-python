data = list(map(int, input().split()))

def logic(l):
    if l[0] == l[-1]:
        return True
    return False

print(logic(data))