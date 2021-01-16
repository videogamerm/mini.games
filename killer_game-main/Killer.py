import time
import random
s1 = open("scores.txt","a")
name = open("name.txt","w")
score = 0
p1 = random.randint(1,4)
p2 = random.randint(1,4)
p3 = random.randint(1,4)
p4=random.randint(1,5)
p5=random.randint(1,4)
p11 = random.randint(1,5)*p3
rs = random.randint(9,12)
sc22 = random.randint(45,55)
while True:
    yk = input("You are the killer type 1,2,3,4 or 5 to kill someone.")
    if yk == "1"or"2"or'4' or '3' or "5" :
        print("person attacked")
        score += sc22
        if yk == '1' or "2" and 3*2*2*2*2 >= sc22 :         
            print ("YOu were REPORTED You Lose one life:(")
            rs-=1
            if rs == 0:
                s1.write(str(score) + " ")
                exit("You Lost And were reported You're score was " + str(score))
    elif score >= p1*p2*p5*2:
        print("You win")
        s1.write(str(score) + " ")
        exit("won")