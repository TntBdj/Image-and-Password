from cryptography.fernet import Fernet

'''
def WriteKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def LoadKey():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

MasterPass = input("Make a master password for all your passwords: ")
x = 3   
def MasterCheck():
    while True:
        global x 
        Check = input(f"\nEnter your master password to verify it's you or quit(q)\nYou have {x} tries left to get your master password right \n    Enter your response: ")
        if Check == MasterPass:
            print("Access granted\n")
            break
        elif Check == "q" or Check == "Q": 
            quit()
        else:
            x = x - 1
        if x == 0:
            print("You used all your tries")
            quit()

key = LoadKey() + (MasterPass.encode())
fer = Fernet(key)

def View():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            UserPass = line.rstrip()
            ShowUser, ShowPass, ShowPhone = UserPass.split("|")
            print("User:", ShowUser, "| Password:", 
                fer.decrypt(ShowPass.encode()).decode(), "| Phone Number:", 
                fer.decrypt(ShowPhone.encode()).decode())

def Add():
    User = input("Enter a username: ")
    Pwd = input("Enter the password: ")
    Phone = input("Enter your phone number: ")
    with open("passwords.txt", "a") as f:
        f.write(User + "|" + fer.encrypt(Pwd.encode()).decode() + "|" + fer.encrypt(Phone.encode()).decode() + "\n")
    print("A new password has been saved.\n\n")


while True:
    Do = input("\nTo view your password enter (v) \nTo add a possword enter (a) \nTo quit enter (q) \n    Enter your response: ").lower()
    if Do == "v":
        MasterCheck()
        View()
    elif Do == "a":
        MasterCheck()
        Add()
    elif Do == "q":
        quit()
    else:
        print("Invalid Input")
        continue
    