lines = int(input())
numbers = []
for _ in range(lines):
    data = list(map(float, input().split()))
    numbers.append(data)

def calculate_bmi(weight, height):
    bmi = weight / height ** 2
    if bmi < 18.5:
        return 'under'
    elif bmi < 25.0:
        return 'normal'
    elif bmi < 30.0:
        return 'over'
    else:
        return 'obese'

result = []
for sub_list in numbers:
    weight, height = sub_list
    bmi_result = calculate_bmi(weight, height)
    result.append(bmi_result)


print(' '.join(x for x in result))
