import random

print("Welcome to Rock-Paper-Scissors")

choice = ["rock","paper","scissors"]

computer = random.choice(["rock","paper","scissors"])
player = input("Enter rock, paper, scissors:")

print("Computer chose:",computer)
print("Player chose:",player)

if computer == player :
    print("It is a tie")
    
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
 
      