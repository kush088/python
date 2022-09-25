import random

player_win=0
computer_win=0

option=["rock","paper","scissors"]
while true:
    user_input=input("Type rock /paper /scissors or q for quite").lower()
    if user_inpur=="q":
        break

    if user_input not in option:
        continue

    random_number=random.randint(0,2)
    #------------------1=rock,2=paper,3=scissors---------------------
    computer_pick=option[random_number]
    print("computer picked",computer_pick+ ".")
     if user_input == "rock" and computer_pick == "scissors":
         print("YOU WON") 
        player_win+=1
     elif user_input == "paper" and computer_pick == "rock":
         print("YOU lose") 
        player_win+=1 
    
    elif user_input == "scissor" and computer_pick == "paper":
         print("YOU WON") 
        player_win+=1 
    elif user_input == "rock" and computer_pick == "scissors":
         print("YOU WON") 
        player_win+=1
    else:
        print(YOU LOSE)

    print("you won",player_win,"times")
    print("computer won",computer_win,"times")           