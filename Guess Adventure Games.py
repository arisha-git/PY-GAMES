#Choose your own adventure

name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You're on a dirt road. \nIt has come to an end and you can either go left or right. \nWhich way do you prefer: ")

if answer == "left":
    answer = input("You come to a river. \nYou can walk around it or swim across it. \nType walk to walk AND swim to swim: ")

    if answer == "swim":
        print("You swam across and were eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles, ran out of energy and lost the game")

    else:
        print("Not a valid option. Game over.")
        
elif answer == "right":
    answer = input("You come t0 a bridge, it looks wobbly. \nDo you want to cross it or head back? (cross/back): ")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. \nDo you talk to them? (yes/no): ")
        if answer == "yes":
             print("You talk to the stranger and they give you gold! You win! Congratulations!")
        elif answer == "no":
            print("You ignored the stranger and lost the gold. You lost!")
        else:
            print("Not a valid option. Game over.")
    else:
        print("Not a valid option. Game over.")
        
else:
    print("Not a valid option. Game over.")

print("Thank you for playing,", name)

#The End
