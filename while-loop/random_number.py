import random
number = random.randint(1, 10)
user_number = int(input("Guess a number between 1 and 10: "))

over = False

while not over:
    if user_number == number:
        print("Congratulations!! You guessed it correct!")
        over = True
    else:
        print("Wrong Guess!! Try Again")
        user_number = int(input("Guess a number between 1 and 10: "))
        
    