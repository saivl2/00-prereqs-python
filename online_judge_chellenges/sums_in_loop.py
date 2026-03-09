nums = int(input())
arr_nums = []
for _ in range(nums):
    numbers = list(map(int, input().split()))
    arr_nums.append(numbers)

total_arr = []
for element in arr_nums:
    total_arr.append(sum(element))

final = ' '.join(str(x) for x in total_arr)
print(final)