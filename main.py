print('''
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to the Treasure Island.")
print("This is the moment you have been waiting for. Your mission is to find the treasure. Good luck and pick your choices carefully.\n") 


#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
crossroad = input("You have come to the Demon's crossroads. Where do you want to go?\nType 'left' or 'right'.").lower()


if crossroad == "left":
  print("You have picked the right option. You will proceed to the next level.")
else:
  print("You fell down a hole. LOL.")
  import sys
  sys.exit()

lake = input("You come across the Lake of Sorrows. What do you want to do?\nType 'swim' or 'wait'.").lower()

if lake == "wait":
  print("You escaped, get ready for the next level.")
else: 
  print("Wrong choice buddy. You were eaten by piranha. HAHA.")
  import sys
  sys.exit()
  
door = input("This is the final round. Pick the door you want to walk through.\nType 'red' or 'blue' or 'yellow'. ").lower()

if door == "yellow":
  print("Congratulations, you have won the game.")
elif door == "red":
  print("You were extremely burned. Apply sunscreen next time. Game over.")
  import sys
  sys.exit()
elif door == "blue":
  print("You were eaten by beasts. Bye Bye.")
  import sys
  sys.exit()
else:
  import sys
  sys.exit()
  
  
