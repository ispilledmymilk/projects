name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road and it has come to an end, would you like to go right or left? ").lower()
if answer == 'left':
    answer = input("You have arrived at a river, would you like to swim across it or walk around it? (swim/walk)")
    if answer == "swim":
        print("You swam across the and got eaten by a croc! ")
    elif answer == "walk":
        print("You walked a lot, ran out of water and lost! ")
    else:
        print("Not a valid option! ")
elif answer == 'right':
    answer = input("You have arrived at a mountain, do you want to climb or walk around it? (climb/walk)").lower()
    if answer == 'climb':
        print("You have reached the top of the mountain and found the treasure chest! ")
    elif answer == 'walk':
        print("You have reached the end of the road and there is no escape! ")
    

else:
    print("Not a valid option! ")
