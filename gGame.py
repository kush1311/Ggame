import random
comp_num=random.randint(0,101)
def esay():
    for att in range(1,12):
        gusse_num=int(input("guasse the number : "))
        if gusse_num<comp_num:
            print("guasse number is low")
            print(f"You have now {att} attempt left ")
            att+=1
        elif gusse_num>comp_num:
            print("guasse number is high")
            print(f"You have now {att} attempt left ") 
            att+=1      
        elif gusse_num==comp_num:
            print("you won number is correct")
            break;
        if att==11:
            print("you loss")
            break;
def hard():
    for att in range(0,7):
        gusse_num=int(input("guasse the number : "))
        
        if gusse_num<comp_num:
            print("guasse number is low")
            print(f"You have now {att} attempt left ")
            att+=1
        elif gusse_num>comp_num:
            print("guasse number is high")
            print(f"You use your{att} attempt left ")   
            att+=1
        elif gusse_num==comp_num:
            print("you won number is correct")
            break;
        if att==6:
            print("you loss")
            break;
starter=input("Enter the level you want to play hard or esay :")
if starter=='hard':
    print("You have 5 attent for gusse the number")
    hard()
else:
    print("you have 10 attent to gusse the number")
    esay()
