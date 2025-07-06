#rock paper scissors game
'''
rock      1
paper    -1
scissors  0
'''
#-----------------------------------------------------------------------------------------------

import random


youDict={"r":1, "p":-1 , "s":0}
revDict={1: "rock 🪨", -1: "paper 📄", 0: "scissors ✂️"}

print(" welcome to rock paper ans scissors")
while True:
    yourchoice=input("enter your choice between 'r','p','s' :")
    you=youDict[yourchoice]

    computer=random.choice([-1,1,0])




    print(f"you chose {revDict[you]}\ncomputer chose {revDict[computer]}")

    if (computer == you ):
       print("thats a draw😐")
    else:
       if (computer == 1 and you == -1):
           print("you win🎉" )
       elif (computer == -1 and you == 0):
           print("you win🎉" )
       elif (computer == 0 and you == 1):
           print("you win🎉" )
    
       elif (computer == -1 and you == 1):
           print("you loose😢" )
       elif (computer == 0 and you ==- 1):
           print("you loose😢" )
       elif (computer == 1 and you == 0):
           print("you loose😢" )
    
       else:
           print("something went wrong")