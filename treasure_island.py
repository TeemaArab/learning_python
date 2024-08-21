
'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''
#
# print("Welcome to the treasure island."
#       " You should find the treasure.")
# step1 = input("You are at the crossroad. Do you want to turn left or right? type 'L or R: \n ").lower()
#
# if step1 == "L":
#     step2 = input("You have come to the lake. Do you want to swim or wait? "
#                 "type Swim or Wait \n").lower()
#     if step2 == "Wait":
#         step3 = input("Do you want to go inside the blue"
#               " door, red door, or yellow door? Type B, R, Y \n").lower()
#         if step3 == "Y":
#             print("You win!")
#         else:
#             print("You lose!")
#     else:
#         print("game over")
# else:
#     print("Game over.")

print("Welcome to the treasure island. You should find the treasure.")
step1 = input("You are at the crossroad. Do you want to turn left or right? Type 'L' or 'R': \n").lower()

if step1 == "l":
    step2 = input("You have come to a lake. Do you want to swim or wait? Type 'Swim' or 'Wait': \n").lower()
    if step2 == "wait":
        step3 = input("Do you want to go inside the blue door, red door, or yellow door? Type 'B', 'R', or 'Y': \n").lower()
        if step3 == "y":
            print("You win!")
        else:
            print("You lose!")
    else:
        print("Game over.")
else:
    print("Game over.")