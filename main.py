import random

def number_wang():
    answer = random.randint(1,10)
    guesses = 0
    while True:
        guess = int(input("What is your number, scrub?: "))
        guesses += 1
        if guess == answer:
            print ("Yup, that's it alright.")
            break
        else:
            if guess < answer:
                print ("Ha, no that's too low.")
            elif guess > answer:
                print ("Ha, no that's too high.")
        if abs((guess - answer)) < 3:
            print ("Getting close.")
        if guesses == 5:
            print ("game over man, game over")
            break
    print (guesses)



number_wang()
