lines = int(input())
numbers = []
for _ in range(lines):
    numbers.append(float(input().strip()))


def dice_rolling(rand_num):
    temp_num = rand_num * 6
    temp_num_int = int(temp_num)
    return temp_num_int + 1

answer = [dice_rolling(x) for x in numbers]
print(' '.join(str(x) for x in answer))