import time
def note():
    remain=input("Enter what do you want to get reminded about")
    timee= float(input("Enter in how many minutes"))
    timee=timee*60
    time.sleep(timee)
    print(remain)
note()