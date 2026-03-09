def cummulative_sum_range():
    prevs = 0
    for num in range(10):
        print(f"The current number {num}, previous number {prevs}, sum is {num + prevs}")
        prevs = num


print(cummulative_sum_range())