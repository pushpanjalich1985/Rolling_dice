#1 Rolling a dice 

# Ask to roll the dice or not
#if yes, generate two random numbers
#print them
#If no, print thankyou
# terminate the program
#else invalid choice
import random


while True:
    choice = input("Roll the dice(y/n): ").lower()  
    #.lower( ) converts the uppercas einto lowercase if the user gave uppercase letter as an input
    if choice == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"({die1}, {die2})") 
    #prints random values for die1 and die2 using f string
    #  - the f-string is doing the job of embedding the values of die1 and die2 directly inside the string.
    elif choice == 'n':
        print("Thankyou for choosing\nProgram terminates")
        break
    else:
      print("INVALID CHOICE!")


