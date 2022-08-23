import random



def gamewin(com,you):
    if(you==com):
        return None
    elif(you=='r'):
        if(com=='p'):
            return False
        elif(com=='s'):
            return True
    
    elif(you=='p'):
        if(com=='r'):
            return True
        elif(com=='s'):
            return False

    elif(you=='s'):
        if(com=='r'):
            return False
        elif(com=='p'):
            return True

 

random_no=random.randint(1,3)
if random_no==1:
    com='r'
elif random_no==2:
    com='p'
elif random_no==3:
    com='s'

you=input("enter rock(r) , paper(p) or scissor(s)")

result=gamewin(com,you)
if result==None:
    print("it's a tie!")

elif result:
    print("You win!")

else:
    print("You Lose!")

print(f"You chose {you} and computer chose {com}")