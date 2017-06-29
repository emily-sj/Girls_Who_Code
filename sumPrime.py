from random import randint

def level3(numlist):
    primeSum=0
    
#part 1: iterate through the list
    for num in numlist:
        prime=True

        #part 2: determine if a prime num
        for x in range (2,num):
            if num%x==0:
                prime= False
        if prime==True:
            print(num)
            primeSum+= num
    #part3: add to the sum
    print("Final number")
    print(primeSum)
    


def level2 (numlist):
    numSum=0
    for num in numlist:
        if num%3==0 or num%5==0:
            print (num)
            numSum+= num
    print ("Final Sum:")
    print(numSum)


#Running code
randomlist=[]
for x in range (100):
    randnumber=randit(10,99)
    randomlist.append(randmunber)

#level2(randomlist)
level3(randomlist)
