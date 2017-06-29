from PIL import Image

#Import the image

myImage = Image.open("poster.jpeg")
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList = []

#pixel manipulation
for pixel in pixelList:
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    newRed = red*3
    if newRed >255:
        newRed = 255
    newGreen = green*1
    if newGreen >255:
        newGreen = 255
    
    newBlue = blue*1
    if newBlue >255:
        newBlue = 255


    p = (newRed,newGreen,newBlue)



    #add pixel to new pixel list
    newPixelList.append(p)


#open the image
newImage = Image.new("RGB", myImage.size)
newImage.putdata(newPixelList)
newImage.show()
