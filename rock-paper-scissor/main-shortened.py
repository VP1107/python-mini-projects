import random

set = {1, -1, 0}
element = random.choice(list(set))

computer = element 
youstr = input("Enter your choice (Stone or Paper or Scissor):")
youDict = {"stone" : 1, "paper" : -1, "scissor" : 0}
reverseDict = {1 : "Stone", -1 : "Paper", 0 : "Scissor"}

you = youDict[youstr.lower()]

#By now we have two variables, you and computer

print(f"You Chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a Draw!")

else:
    if((computer - you) == -1 or (computer - you) == 2):
        print("You Win")
    else:
        print("You Lose")


#we have got this solution by doing (computer-you)