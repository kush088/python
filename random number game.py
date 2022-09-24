import random
random_num=random.randint(1,10)
trial=3
print(random_num)
while trial>0:
    print(f"Attemp remain")
    guess_num=int(input("Enter your number"))
    if guess_num == random_num:
        print("You won the game")
        break
    else:
        trial-=1
    if trial==0:
        print("You lose the game")