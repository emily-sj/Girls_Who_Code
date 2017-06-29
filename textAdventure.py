

#Function
def timeMoney ():
    print("Would you like a job that offers more money or more leisure time")
    answer= input ()
    return answer

#Running Code
print ("What is your name?")
answer= input()

print ("Are you a male or female")
answer = input()
print("Do you want to be a rapper or a model?")
answer= input()
if answer== "rapper" :
    print("You want to become a rapper!")
    a = timeMoney()
    if a=="more leisure time" :
        print ("Would you like to have a one night stand or stay committed?")
        answer= input()
        if answer=="have a one night stand":
            print("Awwwh,now you have to pay child support for the baby.")
        elif answer=="stay committed":
            print("Yay, you live happily ever after with your family.")
    elif a=="more money" :
        print("Would you like to spend your money at the bar or at the casinos?")
        answer = input()
        print ("Awwhh,you get bankrupt!")
    else:
        print("Well, you're going to die old and wrinkly anyway.")
elif answer== "model" :
    print("You want to become a model!")
    a=timeMoney()
    if a=="more leisure time" :
        print("Would you like to watch Netflix or go to a party?")
        answer = input()
        if answer=="watch Netflix" :
            print ("You get fat! Now, your career is over!")
        elif answer=="go to a party" :
            print ("You get into a scandal!Now, your career is over!")
    elif a=="more money" :
        print("Would you like to save your money or spend it on plastic surgery?")
        answer= input()
        print("You have been promoted and get to retire happily in a year!")
    else:
        print("Well, you're going to die old and wrinkly anyway.")

else:
    print ("That's alright.The celeb life isn't for you.")










#close window 

