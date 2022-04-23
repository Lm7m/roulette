
import random


def isodd(x ,userpet ):
    if (x % 2) == 0:
        print("sorry you have lost your pet " ,(userpet))
    else:
         print("congratulation you have win " ,(userpet*2))

def iseven(x ,userpet):
       
    if (x % 2) != 0:
         print("sorry you have lost your pet " ,(userpet))
    else:
         print("congratulation you have win " ,(userpet*2))

def oneto18(x,userpet):
    if x>18:
          print("sorry you have lost your pet " ,(userpet))
    else:
         print("congratulation you have win " ,(userpet*2))

def eighteento36 (x,userpet):
    if x<18:
          print("sorry you have lost your pet " ,(userpet))
    else:
         print("congratulation you have win " ,(userpet*2))


def oneto12(x,userpet):
    if x>13:
          print("sorry you have lost your pet " ,(userpet))
    else:
         print("congratulation you have win " ,(userpet*3))     

def twto24(x,userpet):
    if x>11 & x<25:
          print("congratulation you have win " ,(userpet*3))
    else:
          print("sorry you have lost your pet " ,(userpet))
       

def tfto36(x,userpet):
    if x>23:
        print("congratulation you have win " ,(userpet*3))
    else:
        print("sorry you have lost your pet " ,(userpet))
       

def feelLucky(x,userpet):
    if x==10:
        usernumber = int(input('Please choose number:'))
        if x==usernumber:
            print(" No way!!!! congratulation you have win " ,(userpet*36))
        else:
            print("sorry you have lost your pet " ,(userpet))


print("    welcome to Tneen Roulette     \n \n ")
userpet = int(input(' enter your pet $: '))

print("\n 1- odd \n 2- even  \n 3- red \n 4- black \n 5- 1 to 18 \n 6- 19 to 36")
print(" 7- 1st 12 \n 8- 2nd 12 \n 9- 3rd 12 ")
print(" 10- feel lucky today? enter 10 to select specific number ;) \n")


userSelect = int(input('Please choose only one:'))#user select from the menu


x = int(random.randrange(0, 36, 1)) # generate the random number 

if userSelect == 1 or userSelect==4: #all odds are black
    isodd(x,userpet)
elif  userSelect == 2 or userSelect==3:#all evens are red
    iseven(x,userpet)
elif  userSelect == 5:
     oneto18(x,userpet)
elif  userSelect == 6:
    eighteento36(x,userpet)
elif  userSelect == 7:
    oneto12(x,userpet)
elif  userSelect ==  8:
    twto24(x,userpet)
elif  userSelect ==  9:
    tfto36(x,userpet)
elif  userSelect == 10:
    feelLucky(x,userpet)

    
print("the random nymber is ",x)
