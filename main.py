import random

""" Find the number between 1 to 10 """

mind = random.randint(0,10)
guiss = 0
chance = 0
while guiss!=mind:
    guiss = int(input("Enter your guiss : "))
    if mind == guiss:
        print("You win...")
    elif mind > guiss:
        print("Your guiss number is small...")
    else:
        print("Guiss is high...")
    if chance == 2:
        if guiss != mind:
            print("you loss..")
            print("Correct answer is :",mind)
        break
    chance += 1
