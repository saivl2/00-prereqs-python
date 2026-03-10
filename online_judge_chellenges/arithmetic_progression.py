lines = int(input())
numbers = []
for _ in range(lines):
    data = list(map(int, input().split()))
    numbers.append(data)


def arithmetic_progression(a, b , n):
    result = []
    for i in range(n):
        result.append(a + b * i)
    return sum(result)

new_list = []
for sub_list in numbers:
    a, b, n = sub_list
    new_list.append(arithmetic_progression(a, b, n))
print(' '.join(str(x) for x in new_list))




