import random

computer = random.choice(["rock","paper","scissors"])
player = input("Enter rock, paper, scissors:")

print("Computer chose:",computer)
print("Player chose:",player)

if computer == player :
    print("It is a draw")
    
elif player == "paper":
    if computer == "rock":
        print("Player Win")
    else :
        print("Computer Win")
        
elif player == "rock":
    if computer == "scissors":
        print("Player Win")
    else :
         print("Computer Win")
         
elif  player == "scissors":
     if computer == "paper":
         print("Player Win")
     else :
         print("Computer Win")
else :
      print("Invalid Choice")           