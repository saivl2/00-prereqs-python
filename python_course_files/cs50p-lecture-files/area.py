def main():
   house =  area(50, 20)
   yard =  area(50, 50)
   total = house + yard
   return f"{total} square feet."


def area(l, w):
    return l * w


print(main())