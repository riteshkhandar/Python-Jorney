    
import random
 

num = random.randint(1,101)
print(num)
guess = 0
attempts = 0       

while guess != num:
    guess = int(input("Enter a number: "))
    attempts += 1  

    if guess == num:
        print("You win! You got it in", attempts, "attempts")
    elif guess > num:
        print("Too high!")
    else:
        print("Too low!")
