import time
import random
start1 = ''
start2 = ''
start3 = ''
Doyws = ''




print("You have arrived at Razor Castle.")
time.sleep(1)

while not start1 == 'y' :
    start1 = input("Would you like to go inside (y/n)" )
    time.sleep(3)
    print("""When you go in the Guards take you to the Throne Room
            The Duke has trapped the Princess in a prison.
            There is only one way to get her. Go To Javelin Island Prison!!""")
    Doyws = input(" Do you want a shovel.")
    while not start2 == 'y' :
        start2 = input(" Start adventure to Javelin Island Prison (y/n)")
        while not start3 == 'y' :

            if Doyws == 'y':
                start3 = input("""On your way you see a x on the ground.
                Would you like to unearth what is under? """)
                time.sleep(1)
                print("YAAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!!! You Have Fallen To your Death")
                exit(0)
            start3 = input("You find a forest with a creepy sign on it." + "It Reads: Enter if you dare!! It Leads To Javelin Island Prison.GO in (y/N)")
