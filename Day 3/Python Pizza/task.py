print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill=0

if pepperoni=="y":
    if size == "s":
        bill = 15+2
    elif size == "m":
        bill = 20+3
    else:
        bill = 25+3
if extra_cheese=="y":
    bill+=1
print(f"Your final bill is :${bill}")

