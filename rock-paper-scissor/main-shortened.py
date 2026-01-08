import random

set = {1, -1, 0}
element = random.choice(list(set))

computer = element 
youstr = input("Enter your choice (Stone or Paper or Scissor or End):")
youDict = {"stone" : 1, "paper" : -1, "scissor" : 0}
reverseDict = {1 : "Stone", -1 : "Paper", 0 : "Scissor"}

with open("Score.txt", "w") as f:
    f.write("Round  |  You  |  Computer\n")

y_score = 0
c_score = 0
if not youstr == "end":
    you = youDict[youstr.lower()]

    def game(computer, you):
        print(f"You Chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")
        if(computer == you):
            return None
        if((computer - you) == -1 or (computer - you) == 2):
            return True
        else:
            return False

    def result(game, i=0, y_score=0, c_score=0):
        f = open
        i += 1
        if game:
            print("You Win!!!!")
            f.write(f"Round{i} |  1  |   0\n")
            y_score += 1
        elif game == None:
            print("It's a Draw!")
            f.write(f"Round{i}  0  |   0\n")
        else:
            print("You Lose :((")
            f.write(f"Round{i}  0  |   1\n")
            c_score += 1
    result(game(computer, you, y_score, c_score))


else:
    print(f"Your Score: {y_score}")
    print(f"Computer Score: {c_score}")
    if y_score > c_score:
        print("You Won the Game")
    elif y_score < c_score:
        print("You Lost the Game")  
    else:
        print("It was a Draw")
