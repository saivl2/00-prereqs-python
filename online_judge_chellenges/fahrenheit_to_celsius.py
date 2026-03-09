data = list(map(int, input().split()))
data_items = data[0]

data_f = data[1:]


def f_to_c(l):
    temp_c = [(x - 32) * (5/9) for x in data_f]
    return temp_c

s = ''
for temp in f_to_c(data_f):
    s += str(round(temp)) + ' '

print(s)