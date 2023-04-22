#number guessing game
#Required Libraries
import random
#random library is used to generate a random number.
import math
#math library is used to calculate some mathematical operations.
print("this is number guessing game")
# Taking Inputs from user.
#minimum value
Minimum = int(input("Enter Minimum value:- "))

#maximum value
Maximum = int(input("Enter Maximum value:- "))

# generating random number between the minimum and maximum
x = random.randint(Minimum, Maximum)
#calculate the number of chances to guess the number.
chances=round(math.log(Maximum-Minimum+1,2))

print("\n\tYou've only ",chances," chances to guess the number!\n")

# Initializing the number of guesses is 0.
count = 0

# for calculation of minimum number of
# guesses depends upon range
while count < chances:
    
    count += 1
    
    # taking guessing number as input
    guess = int(input("Guess a number:- "))
    
    # Condition testing
    
    #given compiler generate input is equal to guess input
    if x == guess:
        
        print("Congratulations the number is correct you did it in ",count, " try")
        break

    
    #given compiler generate input is greaterthan to guess input
	    
    elif x > guess:
        print("You guessed too small!")
        
    #given compiler generate input is lessthan to guess input
        
    elif x < guess:
        print("You Guessed too high!")
    print("the  remainig chances are {} ".format(chances-count))
	

# If Guessing is more than required guesses,
#if the number of count value is more than the chances then

# shows this output.
if count >=chances:
	print("\nThe number is " , x)
	print("\tBetter Luck Next time!")

