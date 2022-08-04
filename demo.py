print("\n")
print("Welcome to the Quiz Game!")
print("\n")
choice=input("Do you want to play?\n ")
if choice.lower()!='yes':
    print("We hope You Play this Quiz in future!")
    quit()

score=0
print("\n")
que1=input("What does CPU stands for? \n")
if que1.lower()=='central processing unit':
    print("yay!Your answer is Correct!")
    print("\n")
    score=score+1
else:
    print("Oops! You give wrong answer!")
    print("Correct answer is central processing unit")
    print("\n")

que1=input("What does GPU stand for?\n")
if que1.lower()=='graphics processing unit':
    print("yay!Your answer is Correct!")
    print("\n")
    score=score+1
else:
    print("Oops! You give wrong answer!")
    print("Correct answer is Graphics Processing Unit")
    print("\n")

que1=input("What does RAM stand for?\n")
if que1.lower()=='random access memory':
    print("yay!Your answer is Correct!")
    print("\n")
    score=score+1
else:
    print("Oops! You give wrong answer!")
    print("Correct answer is Random Access Memory")
    print("\n")


que1=input("What does PSU stand for?\n")
if que1.lower()=='power supply':
    print("yay!Your answer is Correct!")
    print("\n")
    score=score+1
else:
    print("Oops! You give wrong answer!")
    print("Correct answer is Power Supply")
    print("\n")

print("Your got "+ str(score)+ " Correct!")
pr=(score/4)*100;
print("Your percentage score is "+ str(pr))


