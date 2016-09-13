import random

print(random.randint(1, 20))
Joels_Age = int(input("How old are you?: "))
Sarahs_age = 34

# Boolean

print(Joels_Age > Sarahs_age)
if Joels_Age > Sarahs_age:
    print ("joel is older than sarah")
elif Joels_Age == Sarahs_age:
    print("you are the same age.")
else:
    print ("You are younger than sarah")
