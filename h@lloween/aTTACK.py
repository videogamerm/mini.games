import time
import random
import os
a = random.randint (1,4)
b = random.randint (1,3)
bc = random.randint (1,4)
pc = random.randint (10,20)
aa = random.randint (1,6)
ad = random.randint (1,10)
atk2 = random.randint (1,5)
atk3 = random.randint (1,15)
health = 0
xp = 0
phealth = 100
attack = ''
attacker = ''



#battle sequence setup

if bc == 1:
    attacker = 'goblin'
    health == 20


if bc == 3 or 2:
    attacker = 'jumpy jack-o-lantern'
    health == 15


if bc == 4:
    attacker = 'sharp shooter skeleton'
    health == 17


print("A " + attacker + " has come up behind you" )
time.sleep(2)
attack = input("Do you want to attack " + attacker + ".{Type attack to attack}")
    #Attack sequence
if attack == 'attack' :
    health =  health - pc
# attacker attack sequence
print(attacker + " is attacking!")
if aa == 1 or 2:
    phealth = phealth - ad
    time.sleep(1)

if aa == 3 or 4 :
    phealth = phealth - atk2
    time.sleep(1)

if aa == 5 or 6:
    phealth = phealth - atk3
    time.sleep(1)
    print("Your health is " + str(phealth))
    #check if won
if (health <= 3):
    print("The " + attacker + " has been defeated")
    health = 0
    xp = xp + a + b
    print("You gained "+ str(xp) + " xp")
    os.system("python3 razorCastle.py")
else:
    print("You lose")
    exit(0)
