'''
1 for snake
-1 for water

0 for gun
'''
import random

def game():
    computer = (random.choice([-1,0,1]))
    youDict = {"s" : 1,"g": 0,"w": -1}
    reverseDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}
    youstr = (input("Enter your choice:{s for Snake, w for Water, g for Gun}:  "))
    if youstr not in youDict:
         print("Invalid input! Please choose among s,w,g. ")
         game()
    else:
        you = youDict[youstr]
        print(f"You chose:  {reverseDict[you]}\nComputer chose: {reverseDict[computer]}")
        if (computer == you):
                        print("Draw...Try Again.")
        else:
            if(computer == -1 and you == 1):
                print("Hurray! You WON.")
                            
            elif (computer == -1 and you == 0):
                print("Oops! Better luck next time.")

            elif(computer == 1 and you == -1):
                print("Oops! Better luck next time.")

            elif (computer == 1 and you == 0):
                print("Hurray! You WON.")

            elif (computer == 0 and you == 1):
                print("Oops! Better luck next time.")

            elif (computer == 0 and you == -1):
                print("Hurray! You WON.")

            else:
                print("Something went wrong")

        ques = input("Wanna try again?(Y/N): ")
        if ques.lower() =="y":
            game()
        else:
            print("Well played! "+name)
        return
    
print("Welcome to 🐍 Snake 💧 Water 🔫 Gun Game!")
name = input("Enter your name: ")
game()
    