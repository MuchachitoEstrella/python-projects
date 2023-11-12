hasdata = False
hasage = False
attempt = int(0)

while hasdata == False:
    try:
        age1 = float(input("enter your age: "))
        age2 = float(input("enter the age of the person who you want to kow when you will be half their age: "))
        rate = float(input("enter a rate (I recommend 0.1 but anything lower than 1 will do): "))
        hasdata = True
    except:
        print("please try again")

print("\nthis could take a while . . .")

if age1 == age2 / 2:
    print("\nyou are half their age already")
elif age1 > age2 / 2:
    print("\nyou are already more than half")
else:
    while hasage == False:
        if age1 >= age2 / 2:
            hasage = True
        else:
            age1 += rate
            age2 += rate
            attempt += 1

input(f"\nthis is how old you would be: {age1}\nthis is how old they would be {age2}\nthis is how many attempts it took to find out: {attempt}\n\npress enter to exit")