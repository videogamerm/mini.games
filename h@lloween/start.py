import time
import random
import os
start = ''
start1 =''
om =''
start2=''
start3=''
ac = random.randint (1,4)
attack = ''
name = input("What is your name?Important messages will be in curly braces({}) ")
print("Hello " + name + " Welcome to h@ll0ween")
while not start  == 'y':
    start=input("Ready to start (y/n) ")
    time.sleep(2)
    print("The King wants to tell you someting")
    time.sleep(2)
    print("Hello " + name + ".This is the King of Jack-0 lanternworld. You must be the new kid from the nearby village.")
    time.sleep(2)
    print("Would you like to check the mailbox")
    while not start1  == 'y':
        start1 = input("Open mailbox (y/n) ")
        time.sleep(2)
        while not om  == 'y':
            om = input("There is an envolope addresed to you. Would you like to open it (y/n)")
            time.sleep(2)
            while not start2  == 'y':
                start2 = input("The letter reads 'Dear " + name + """,
                The Duke of Raptorcity requests to meet with you at 6:00 P.M. at Razor castle for Important matters.
                -The Duke of Raptorcity's Messenger'
                King:Should you go to Razor castle? (y/n)""")
                time.sleep(2)
                print("""Okay, I'll Send you with one guard on your journey
                (King leaves, One soldier stays) """)
                input("Start Journey? (y/n)")
                if start3  == 'y':
                    time.sleep(2)
                    os.system("python3 aTTACK.py")

                if start2 == 'n':
                    print("Messenger:Okay," + name + """I will tell the Duke.(Leaves Room)
                    {(The Duke of Raptorcity has gotten mad and sent assasins to kill you)YOU LOSE}""")
                    exit("OOF!")
