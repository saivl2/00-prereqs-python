num = int(input())
numbers = list(map(int, input().split()))


def weighted_sum(num):
    l = []
    for n, i in enumerate(str(num)):
        l.append((n + 1) * int(i))
    return sum(l)
# print(weighted_sum(9))

s = ''
for number in numbers:
    #print(type(weighted_sum(number)))
    s += str(weighted_sum(number)) + ' ' 
print(s)
        

