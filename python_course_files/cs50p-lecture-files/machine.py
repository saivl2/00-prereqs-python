emoticon = "v.v"

def main():
    # In this main function, change the emotion of the emoticon variable
    global emoticon
    say('Is anyone there?')
    emoticon = ':D'
    say("Oh hi!")

def say(phrase):
    print(f"{phrase} {emoticon}")


main()