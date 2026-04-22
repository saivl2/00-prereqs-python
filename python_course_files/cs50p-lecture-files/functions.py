def main():
    name = input("What's your name? ").strip().title()
    #hello(name)
    hello()


def hello(user_name = 'World'): # Default parameter, this is used if no argument is given
    print(f"Hello {user_name}")


main()