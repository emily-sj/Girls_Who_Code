from random import randint

#Funtions



#Running Code

numlist=[]
for x in range (100):
    num=randint (10,99)
    num2=randint (10,99)
    if (num%5==0) and (num2%3==0):
        sum=num+num2
        numlist.append(sum)
        #numSum+=n
print("Final Sum:")
print (numlist)
