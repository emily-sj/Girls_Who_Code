from PIL import Image

##Functions
def blackWhite(pixel):
    red=pixel[0]
    green=pixel[1]
    blue=pixel[2]
    avg=(red+green+blue)//3

    newRed=avg
    
    newGreen=avg
   
    newBlue=avg
    p=(newRed, newGreen, newBlue)
    newPixelList.append(p)


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

def red(pixel):

#pixel manipulation
    red=pixel[0]
    green=pixel[1]
    blue=pixel[2]

    newRed=red*2
    if newRed >255:
        newRed=255
    p=(newRed, green, blue)
    

#add pixel to new pixel list
    newPixelList.append(p)

def negative(pixel):
    red=pixel[0]
    green=pixel[1]
    blue=pixel[2]


    newValue1=(255- red)
    newValue2=(255-green)
    newValue3=(255-blue)
    p=(newValue1,newValue2,newValue3)

    newPixelList.append(p)

def blue(pixel):

    #pixel manipulation
    red=pixel[0]
    green=pixel[1]
    blue=pixel[2]

    newBlue=blue*2
    if newBlue >255:
        newBlue=255
    p=(red, green, newBlue)
    

    #add pixel to new pixel list
    newPixelList.append(p)

    
    




#import the image
myImage= Image.open("ele2.jpg")
imageData = myImage.getdata ()
pixelList= list(imageData)

newPixelList=[]

length = len(pixelList)
third=length//3
third2=third*2
#third2=length

counter=0
for pixel in pixelList:
    #pixel manipulation

    if (counter<third):
        red(pixel)
    elif (counter<third2):
        blackWhite(pixel)
    else:
        blue(pixel)
    counter+=1
##
##
##        
##    if (counter<third): #this is the top half of the photo
##        half=length//2
##        if (counter>half):
##            blackWhite(pixel)
##        if (counter<half):
##            blue(pixel)
##            counter=counter+1
##            
##            
##            
##            
##            
##    
##        
####
####    else: #this is the bottom half
##        negative(pixel)
##
##    counter=counter+1
        
    
    

#open the image
newImage=Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()
#newImage.save("newPhoto.jpeg","jpeg")
