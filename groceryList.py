#groceryList= ["cake","cookies", "cupcakes","milk", "eggs"]
groceryList= []
while True:
    print("Do you want to add an item to your list? (y/n)")
    answer= input ()
    if answer==("y"):
        print ("What would you like to add to your list?")
        answer= input ()
        groceryList.append(answer)
    if answer==("n"):
        print ("Okay!Your grocery list is:")
        for x in groceryList:
            print (x)
        break 

    
    

    
    
