nums = int(input())
numbers = list(map(int, input().split()))

total = 0
for item in numbers:
    total += item
print(total)
