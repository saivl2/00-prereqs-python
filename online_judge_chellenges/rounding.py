nums = int(input())
full_nums = []
for _ in range(nums):
    numbers = list(map(int, input().split()))
    full_nums.append(numbers)

decimal_nums = []
for arr in full_nums:
    decimal_nums.append(arr[0] / arr[1])

rounded_nums = []
for x in decimal_nums:
    if x > 0:
        rounded_nums.append(int(x + 0.5))
    elif x < 0:
        rounded_nums.append(int(x - 0.5))
    else:
        rounded_nums.append(0)

str_nums = ' '.join(str(x) for x in rounded_nums)
print(str_nums)