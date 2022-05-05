"""
1) 3-5 Sentences of how the overall goal of the script
The overall goal of this project scrpit is to teach how to use the PIL/pillow library to alter certain images.
It allows us to practive the different uses of imported libraries and how they can make our lives a lot easier for the future.
It'll help prepare us for the next project which will be usinging those altered images to make a 2D game

2) Point form layout of the structure of the code in plain English
- find the images we want to use
- define all the different ways they can change the picture/images
- create the initial layout to the logic of the program
- insert variables into the logic


"""
from PIL import Image
import os, sys

def Size():
    pass
def Type(f):
    for f in os.listdir("."):
        if f.endswith(".jpg"):
            i = Image.open(f)
            fn, fext = os.path.splitext(f)
            i.save("png folder/{}.png".format(fn))

def Rotation():
    pass
def Color():
    pass
def Transparency():
    pass 
Change = ""
while Change != "q":
    UserChoice = int(input("What dragon image do you want (1-10): "))
    if UserChoice > 0 or UserChoice < 10:
        break
    else:
        print("Invalid Input")
RandomImage = Image.open(f"dragon {UserChoice}.jpg")
RandomImage.show()
while Change != "q":
    Change = input("What would you like to change anything about this image (size, type, rotation, color, transparency) or (q) to quit: ").lower()
    if Change == "size":
        Size()
    elif Change == "type":
        Type(RandomImage)
    elif Change == "rotation":
        Rotation()
    elif Change == "color":
        Color()
    elif Change == "transparency":
        Transparency()
