income = int(input())
tax = 0
if income <= 10_000:
    tax = 0
elif income <= 20_000:
    tax = (income - 10000) * 10 / 100
else:
    tax = 0 + (10000 * 10 / 100) 
    tax += (income - 20000) * 20 / 100
    
print(tax)