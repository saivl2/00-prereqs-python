num = int(input('Enter n: '))
prod = 1
for i in range(1, num + 1):
    prod *= i
    i -= 1 
print(prod)