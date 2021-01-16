import random
import time
score = 0
while True:
  s=input("M for multiplication,D for division,A for addition and S for subtaction.")
  if s == "M":
    x = random.randint(1,12)
    y = random.randint(1,12)
    pr = x*y
    input a=("Whats " + x+" x " + y)
      if a == pr:
        print("Great job!!!!!")
        score += 2
      else:
      print("Oops")
      score -= 1  
  if s == "D":
    x = random.randint(1,50)
    y = random.randint(1,50)
    
    if x%y <=1:
      sleep(5)
    else:
      input a=("Whats " + x+" ÷ " + y)
       if a == pr:
         print("Great job!!!!!")
         score += 2
       else:
         print("Oops")
         score -= 1  
  if s == "A":
  x = random.randint(1,30)
    y = random.randint(1,30)
    pr = x+y
    input a=("Whats " + x+" + " + y)
      if a == pr:
        print("Great job!!!!!")
        score += 2
      else:
      print("Oops")
      score -= 1  
  if s =="S":
  x = random.randint(1,12)
    y = random.randint(1,11)
    pr = x-y
    input a=("Whats " + x+" - " + y)
      if a == pr:
        print("Great job!!!!!")
        score += 2
      else:
      print("Oops")
      score -= 1  
