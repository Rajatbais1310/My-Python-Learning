
"""Guess The Number Game Devoloped By Rajat Bais"""

n=25
number_of_guess=0
print("You Have 10 Guesses To Guess The Correct One\n")
while(number_of_guess<10):
    n = int(input("Enter Your Guess\n"))
    number_of_guess = number_of_guess + 1
    print(10 - number_of_guess, "no. of Guesses left")
    if n<25:
        print("Your Guess is Wrong Enter Greater Number")
    elif n>25:
        print("Your Guess is Wrong  Enter Smaller Number")
    elif n==25:
        print("You Won")
        print("You Take :",number_of_guess, "Guesses")
        break
        # z = input("Do You Want To Play Again Y/N?")
        # if z == "y":
        #     continue
        # if z == "n":
        #     break
    if (number_of_guess>=10):
        print("Game Over")
        # z = input("Do You Want To Play Again Y/N?")
        # if z == "y":
        #     continue
        # if z == "n":
        #     break
