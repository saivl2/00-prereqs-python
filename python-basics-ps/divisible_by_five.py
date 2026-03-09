data = list(map(int, input().split()))

def check_div_5(l):
    div_by_5 = []
    for item in l:
        if item % 5 == 0:
            div_by_5.append(item)
    return div_by_5

print(check_div_5(data))
