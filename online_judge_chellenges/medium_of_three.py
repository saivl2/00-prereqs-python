lines = int(input())
numbers = []
for _ in range(lines):
    data = list(map(int, input().split()))
    numbers.append(data)

def medium_of_three(li):
    med = 0
    li.sort()
    return li[1]

result = []
for sub_list in numbers:
    result.append(medium_of_three(sub_list))

print(' '.join(str(n) for n in result))

    