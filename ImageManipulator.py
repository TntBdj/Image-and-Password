"""
1) 3-5 Sentences of how the overall goal of the script
The overall goal of this project scrpit is to teach how to use the PIL/pillow library to alter certain Ims.
It allows us to practive the different uses of imported libraries and how they can make our lives a lot easier for the future.
It'll help prepare us for the next project which will be usinging those altered Ims to make a 2D game

2) Point form layout of the structure of the code in plain English
- find the Ims we want to use
- define all the different ways they can change the picture/Ims
- create the initial layout to the logic of the program
- insert variables into the logic


"""

from PIL import Image, ImageFilter
import os, sys, glob

#The function that calls all functions HAHAHH 
#Basically seeing what they want to do or if they want to quit
def Modes():
    while True:
        Mode = input("Would you like to edit image all at once(1), one specific thing(2), open all images(3) or (q) to quit: ")
        if Mode == "1":
            Everything()
        elif Mode == "2":
            Options()
        elif Mode == "3":
            Open()
        elif Mode == "q":
            quit()
        else:
            print("invalid input")

#Me trying the bonus
def Everything():
    while True:
        EveryOption = input("size, type, rotation, color, transparency: ")
        if EveryOption == "size":
            while True:
                try:
                    SizeChoice = int(input("Between 200X200(2), 400X400(4) and 600X600(6), what size you want: "))
                    break
                except ValueError:
                    print("invalid input")
            Im = Image.open(f"dragon {UserChoice}.jpg")
            if SizeChoice == 2:
                Im.thumbnail(x200)
                break
            elif SizeChoice == 4:
                Im.thumbnail(x400)
                break
            elif SizeChoice == 6:
                Im.thumbnail(x600)
                break
            else:
                print("Invalid input")
        elif EveryOption == "type":
            Im = Image.open(f"dragon {UserChoice}.jpg")
            fn, fext = os.path.splitext(f"dragon {UserChoice}.jpg")
        elif EveryOption == "rotation":
            Rotation()
        elif EveryOption == "color":
            Color()
        elif EveryOption == "transparency":
            Transparency()
        elif EveryOption == "n":
            break
        else:
            print("Invalid input")

#All the options to alter Ims with functions of each options to make it more organized
def Options():
    while True:
        Change = input("What would you like to change anything about this image (size, type, rotation, color, transparency) or (n) for nothing: ").lower()
        if Change == "size":
            Size()
        elif Change == "type":
            Type()
        elif Change == "rotation":
            Rotation()
        elif Change == "color":
            Color()
        elif Change == "transparency":
            Transparency()
        elif Change == "n":
            break
        else:
            print("Invalid input")

#changine the size
def Size():
    x200 = (200, 200)
    x400 = (400, 400)
    x600 = (600, 600)
    while True:
        while True:
#making sure its a number
            try:
                SizeChoice = int(input("Between 200X200(2), 400X400(4) and 600X600(6), what size you want: "))
                break
            except ValueError:
                print("invalid input")
#seeing if the number is an actual option to change
        try:
            os.mkdir("Size 200")
            os.mkdir("Size 400")
            os.mkdir("Size 600")
        except:
            pass
        Im = Image.open(f"dragon {UserChoice}.jpg")
        if SizeChoice == 2:
            Im.thumbnail(x200)
            Im.save('Size 200/'+Name+'200.jpg')
            print("Saved in folder (Size 200)\n")
            break
        elif SizeChoice == 4:
            Im.thumbnail(x400)
            Im.save('Size 400/'+Name+'400.jpg')
            print("Saved in folder (Size 400)\n")
            break
        elif SizeChoice == 6:
            Im.thumbnail(x600)
            Im.save('Size 600/'+Name+'600.jpg')
            print("Saved in folder (Size 600)\n")
            break
        else:
            print("Invalid input")

#changing the type of photo fpg to png
def Type():
    try:
        os.mkdir("PNG")
    except:
        pass
    Im = Image.open(f"dragon {UserChoice}.jpg")
    fn, fext = os.path.splitext(f"dragon {UserChoice}.jpg")
    Im.save('PNG/{}.png'.format(fn))
    print("Saved in folder (PNG)\n")

#rotating left in degrees
def Rotation():
    try:
        os.mkdir("Rotation")
    except:
        pass
    while True:
        try:
            Degrees = int(input("Rotate left how many degrees: "))
            break
        except ValueError:
            print("Invalid input\n")
    Im = Image.open(f"dragon {UserChoice}.jpg")
    Im.rotate(Degrees).save("Rotation/"+Name+"")
    print("Saved in folder (Rotation)\n")

#simple black and white photo change
def Color():
    try:
        os.mkdir("BlackWhite")
    except:
        pass
    Im = Image.open(f"dragon {UserChoice}.jpg")
    Im = Im.convert("L")
    Im.save("BlackWhite/"+Name+"")
    print("Saved in folder (BlackWhite)\n")

#Adding blur to the Im that the user can input
def Transparency():
    try:
        os.mkdir("Blur")
    except:
        pass
    while True:
        try:
            BlurAmount = float(input("How much would you like to blur (Choose a number)?: "))
            break
        except ValueError:
            print("Invalid input\n")
    Im = Image.open(f"dragon {UserChoice}.jpg")
    OtherImage = Im.filter(ImageFilter.GaussianBlur(BlurAmount))
    OtherImage.save("Blur/"+Name+"")
    print("Saved in folder (Blur)\n")

def Open():
    FolderList = ["Size 200", "Size 400", "Size 600", "PNG", "Rotation", "BlackWhite", "Blur"]
    for i in FolderList:
        try:
            images = os.listdir(i)
            print(f"Image in the {i} Directory are: ")
            print (images)
            print("")
            All = Image.open(f"{i}\{images}")
            print(f"{i}\{images}")
            All.show()
            
        except:
            pass

#Technically the start of the code
#seeing what image they want to change
while True:
    UserChoice = int(input("What dragon image do you want (1-10): "))
    if UserChoice > 0 or UserChoice < 10:
        break
    else:
        print("Invalid Input")
RandomIm = Image.open(f"dragon {UserChoice}.jpg")
Name = (f"dragon {UserChoice}.jpg")
RandomIm.show()
Modes()
