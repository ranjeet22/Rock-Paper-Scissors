import random
table = {"r":1,"p":2,"s":3}
revtable = {1:'ROCK',2:'PAPER',3:'SCISSOR'}
print('''
Hey Player welcome to the GAME of...
ROCK  PAPER SCISSOR
before we start the game...
''')
choice = input("Enter your choice : ")
computer = random.randint(1,3)
player = table[choice]
print(f"COMPUTER CHOSE {revtable[computer]}\nPLAYER CHOSE {revtable[player]}")

if(computer==player):
    print("MATCH DRAW");
elif(computer==1 and player==2):
    print("YOU WON")
elif(computer==1 and player==3):
    print("YOU LOST!")
elif(computer==2 and player==1):
    print("YOU LOST!")
elif(computer==2 and player==3):
    print("YOU WON")
elif(computer==3 and player==1):
    print("YOU WONT!")
elif(computer==3 and player==2):
    print("YOU WON")
