#QUIZ GAME (easy)

print("Welcome to this computer quiz")
playing= input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
  
  
print("Let's play :D ")
print("Answers to be entered in ALL CAPS!")
score = 0

answer = input("1. What does CPU stand for? ")
if answer.upper() == "CENTRAL PROCESSING UNIT":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("2. What does GPU stand for? ")
if answer.upper() == "GRAPHICS PROCESSING UNIT":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("3. What does RAM stand for? ")
if answer.upper()== "RANDOM ACCESS MEMORY":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("4. What does PSU stand for? ")
if answer.upper() == "POWER SUPPLY":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print("\n")
print("You got " + str(score) + " questions correct")
print("You got " + str((score/4)*100) + "%")
