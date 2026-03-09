def main():
    a = int(input())
    b = int(input())

    return calc(a,b)

def calc(a, b):
    if a * b <= 1000:
        return a * b
    else:
        return a + b
    
result = main()
print(result)