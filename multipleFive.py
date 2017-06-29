from random import randint

#Funtions



#Running Code

numlist=[]
for x in range (100):
    num=randint (10,99)
    if num%5==0:
        numlist.append(num)
    
print (numlist)
