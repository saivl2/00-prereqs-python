nums = int(input())
arr_nums = []
for _ in range(nums):
    numbers = list(map(int, input().split()))
    arr_nums.append(numbers)
# print(arr_nums)

# Main code
min_list = []
for item in arr_nums:
    min_list.append(min(item))

final_list = ' '.join(str(i) for i in min_list)
print(final_list)