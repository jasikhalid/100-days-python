import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps=random.randint(0,2)
yrps=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if yrps == 0:
    print("You choose rock")
    print(rock)
    if rps==1:
        print("Computer choose paper")
        print(paper)
        print("Computer wins")
    elif rps==2:
        print("Computer choose scissors")
        print(scissors)
        print("You wins")
    else:
        print("Computer choose rock")
        print(rock)
        print("Draw")
elif yrps==1:
    print("You choose paper")
    print(paper)
    if rps == 1:
        print("Computer choose paper")
        print(paper)
        print("Draw")
    elif rps == 2:
        print("Computer choose scissors")
        print(scissors)
        print("Computer wins")
    else:
        print("Computer choose rock")
        print(rock)
        print("You wins")
elif yrps==2:
    print("You choose scissors")
    print(scissors)
    if rps == 1:
        print("Computer choose paper")
        print(paper)
        print("You wins")
    elif rps == 2:
        print("Computer choose scissors")
        print("Draw")
    else:
        print("Computer choose rock")
        print(rock)
        print("Computer wins")
else:
    print("You choose a invalid number,You LOOSE")

