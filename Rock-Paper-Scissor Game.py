import random

def game():
    tot=int(input("Enter the total points of the game:"))
    lst=['R','P','S']
    pt1=0
    pt=0
    while True:
        ch=input("Enter choice R,P or S")
        if ch in lst:
            comp=random.choice(lst)
            if comp=='R':
                if ch=='P':
                    print("You get one point")
                    pt+=1
                if ch=='R':
                    print("It's a tie")
                else:
                    print("Computer gets one point")
                    pt1+=1
            elif comp=='S':
                if ch=='R':
                    print("You get one point")
                    pt+=1
                elif ch=='S':
                    print("It's a tie")
                else:
                    print("Computer gets one point")
                    pt1+=1
            else:
                if ch=='S':
                    print("You get one point")
                    pt+=1
                elif ch=='P':
                    print("It's a tie")
                else:
                    print("Computer gets one point")
                    pt1+=1
        else:
            print("Invalid choice")
        if pt==tot:
            print("You win!")
            break
        elif pt1==tot:
            print("Computer win")
            break
    con=input("Would you like to continue playing the game?y/n")
    if con=='y':
        game()
    else:
        print("THANK YOU VISIT AGAIN")
        


print("WELCOME TO ROCK-PAPER-SCISSOR GAME!")

game()

        
        

