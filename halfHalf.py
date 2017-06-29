from PIL import Image

##Functions
def negative(pixel):
    red=pixel[0]
    green=pixel[1]
    blue=pixel[2]
    avg=(red+green+blue)//3

    newRed=avg
    
    newGreen=avg
   
    newBlue=avg
    p=(newRed, newGreen, newBlue)
    newpixelList.append(p)


def overExpose(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]


    newRed = red*2
    if newRed > 255:
        newRed = 255

    newGreen = green*2
    if newGreen > 255:
        newGreen = 255

    newBlue = blue*2
    if newBlue > 255:
        newBlue = 255
    p = (newRed,newGreen,newBlue)
    newpixelList.append(p)



#import the image
myImage= Image.open("ele2.jpg")
imageData = myImage.getdata ()
pixelList= list(imageData)

newpixelList=[]

length = len(pixelList)
halfway=length//2


counter=0
for pixel in pixelList:
    #pixel manipulation
    
    if (counter<halfway): #this is the top half of the photo
        overExpose(pixel)
        

    else: #this is the bottom half
        negative(pixel)

    counter=counter+1
        
    



#create new pixel


    

   
    
    



#add pixel to new pixel list
    

#open the image
newImage=Image.new("RGB",myImage.size)
newImage.putdata(newpixelList)
newImage.show()
#newImage.save("newPhoto.jpeg","jpeg")
