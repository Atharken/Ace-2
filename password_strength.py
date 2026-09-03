# password strength checker
import string

while True:

    upper = 0
    lower = 0
    number = 0
    symbol = 0
  
    
    p = input("enter your password \n:")
    
    if len(p) < 8:
        print("password must have minimum of 8 character !")
        continue 
        
    for i in p:   #to check letter one by one

        if i.isupper():
    
            upper += 1

        elif i.islower():
            
            lower += 1

        elif i.isdigit():
           
            number += 1

        elif i in string.punctuation:
            
            symbol += 1
            
    total = 0 # total is out of for loop so it didn't  reset with each alphabet

    if upper > 0:
      total += 1

    if lower > 0:
      total += 1

    if number > 0:
      total += 1

    if symbol > 0:
      total += 1
        
    if total == 1:
        print("password is very weak")
    elif total == 2:
        print("password is weak")
    elif total == 3:
        print("password is bit strong")
    elif total >= 4:
        print("password is strong")