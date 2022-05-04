from PIL import Image
UserChoice = 0
while UserChoice != "100": 
    while True:
        UserChoice = int(input("What dragon image do you want (1-10): "))
        if UserChoice > 0 or UserChoice < 10:
            break
        else:
            print("Invalid Input")
    RandomImage = Image.open(f"dragon {UserChoice}.jpg")
    RandomImage.show()
