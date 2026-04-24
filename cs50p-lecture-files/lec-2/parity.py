def main():
    x = int(input("Enter x: "))
    if is_even(x):
        return "Even"
    else:
        return "Odd"
    
def is_even(n):
    return n % 2 == 0

print(main())