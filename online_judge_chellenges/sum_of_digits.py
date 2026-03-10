lines = int(input())
numbers = []
for _ in range(lines):
    data = list(map(int, input().split()))
    numbers.append(data)


def calculate_formula(l):
    result = []
    for sub_list in l:
        a, b, c = sub_list
        result.append(a * b + c)
    return result

# print(calculate_formula(numbers))

def sum_of_digits(num):
    total = 0
    for n in str(num):
        total += int(n)
    return total

# print(sum_of_digits(100))

answer = []
for num in calculate_formula(numbers):
    answer.append(sum_of_digits(num))

print(' '.join(str(x) for x in answer))