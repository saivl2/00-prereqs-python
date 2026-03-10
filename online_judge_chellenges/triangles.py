lines = int(input())
numbers = []
for _ in range(lines):
    data = list(map(int, input().split()))
    numbers.append(data)

def is_triangle(li):
    a, b, c = li
    if a + b > c and b + c > a and a + c > b:
        return 1
    else:
        return 0
    
result = []
for sub_list in numbers:
    result.append(is_triangle(sub_list))

print(' '.join(str(x) for x in result))
