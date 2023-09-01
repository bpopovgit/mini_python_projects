print("Welcome to my computers quiz!")

playing = input("Would you like to play? ")

if playing.lower() != "yes":
    print("See you next time!")
    quit()

print("Okay! Let's play!")
score = 0

answer = input("What does BIOS stand for? ")
if answer.lower() == "basic input output system":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("What does LCD stand for? ")
if answer.lower() == "liquid crystal display":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Your answered " + str(score) + "questions correctly.")
print("You got " + str((score / 4) * 100) + "%.")
