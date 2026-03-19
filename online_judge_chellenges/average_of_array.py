lines = int(input())
numbers = []
for _ in range(lines):
    data = list(map(int, input().split()))
    numbers.append(data)

def average_arr(arr):
    if arr[-1] == 0:
        arr = arr[:-1]
    avg = sum(arr) / len(arr)
    return avg

answer = []
for i in numbers:
    answer.append(int(average_arr(i)))

print(' '.join(str(x) for x in answer))