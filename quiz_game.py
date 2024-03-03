print("Welcome to my computer quiz!")

playing = input("Do you want to play this game? ")

if playing.lower() != "yes":
    quit()
    
print("Okay! Lets play:) ")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Your answer is correct!')
    score+=1
else:
    print("Your answer is incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Your answer is correct!')
    score+= 1
else:
    print("Your answer is incorrect!")

answer = input("What does RAM stand for?  ")
if answer.lower() == "random access memory":
    print('Your answer is correct!')
    score += 1
else:
    print("Your answer is incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('Your answer is correct!')
    score+=1

else:
    print("Your answer is incorrect!")
    
print("You got " + str(score) + " questions correct")
print("You got " + str((score/4)*100) + " %")
