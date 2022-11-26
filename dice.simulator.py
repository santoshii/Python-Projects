import random
def simulator():
    print("press 1 to roll dice")
    print("press 2 to exit the game")
    while True:
        number=int(input("Enter your choice: "))
        if number==1:
            n=random.randint(1, 6)
            print(n)
            choice=input("Do you want to roll dice again enter yes or else enter no: ").upper()
            if choice=="yes".upper():
                continue
            else:
                break
        else:
            break
simulator()