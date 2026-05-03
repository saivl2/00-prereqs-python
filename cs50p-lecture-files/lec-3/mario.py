def main():
    print_square(3)


def print_square(dim):
    # For each row in square
    for i in range(dim):
        # For each brick in row
        for row in range(dim):
            # Print brick
            print('#', end = '')
        print()

main()