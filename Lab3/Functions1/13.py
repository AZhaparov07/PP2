import random
def guessthenum():
    word = input("Hello! What is your name?\n")
    print(f"Well, {word}, I am thinking of a number between 1 and 20.")
    counter = 0
    guessingnum = random.randint(1,20)
    while True:
        print("Take a guess.")
        num = int(input())
        counter += 1
        if(num < guessingnum):
            print("Your guess is too low.")
        elif(num > guessingnum):
            print("Your guess is too high.")
        else:
            print(f"Good job, KBTU! You guessed my number in {counter} guesses!")
            break
guessthenum()