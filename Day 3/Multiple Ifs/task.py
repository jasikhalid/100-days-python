print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill=5
        print("Please pay $5.")
    elif age <= 18:
        bill=7
        print("Please pay $7.")
    else:
        bill=12
        print("Please pay $12.")
    photo=input("If you want a photo click Y you didnt click N")
    if photo=="y":
        bill+=3
    print(f"your total amount to pay {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
