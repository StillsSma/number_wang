import random

def number_wang():
    answer = int(input("Beep Boop choose your number between 0 and 100, and I will guess it. Boop. : "))
    num_guesses = 0
    low = 0
    high = 100
    guess = random.randint(low,high)
    while True:

        num_guesses += 1
        guess = random.randint(low,high)
        print (guess)
        if guess < answer:
            print ("Ha, no that's too low.")
            low = guess + 1
        elif guess > answer:
            print ("Ha, no that's too high.")
            high = guess - 0
        else:
            print ("Yup, that's it alright.")
            break

        if abs((guess - answer)) < 5:
            print ("Getting close.")
        if num_guesses == 5:
            print ("IMPOSSIBLE!!! Beep! ")
            break
    print (num_guesses)

number_wang()
