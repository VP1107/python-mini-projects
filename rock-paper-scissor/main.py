'''
1 for Stone
-1 for Paper
0 for Scissor
'''

import random

set = {1, -1, 0}

computer = random.choice(list(set))
youstr = input("Enter your choice (Rock = r or Paper = p or Scissor = s or Quit = q):").lower()
youDict = {"r" : 1, "p" : -1, "s" : 0}
reverseDict = {1 : "Rock", -1 : "Paper", 0 : "Scissor"}

if (youstr == "q"):
    print("Thank You for Playing")
else:
        you = youDict[youstr.lower()]

        print(f"You Chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")


        if (youstr != "r" and youstr != "p" and youstr != "s"):
                print("Invalid Input!!")
                print("Please Enter (r, p, or s) ")


        elif(computer == you):
                print("It's a Draw!")


        else:
                if(computer == -1 and you == 1):   
                        print("You Lose!")

                elif(computer == -1 and you == 0): 
                        print("You Win!")

                elif(computer == 1 and you == -1):  
                        print("You Win!")

                elif(computer == 1 and you == 0):   
                        print("You Lose!")

                elif(computer == 0 and you == -1):  
                        print("You Lose!")

                elif(computer == 0 and you == 1):   
                        print("You Win!")

                else:
                        print("Something Went Wrong!!")









    

    
