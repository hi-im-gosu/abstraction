import random

input("Abstraction of REFUGEE ESCAPE.")

#Choice of Advanced or Basic Abstraction
methodOfAbstraction = input("""    1. Advanced Abstration
    2. Basic Abstraction""")

def choiceOfOneOrTwo(x):
    for i in range(100):
        if x != "1" and x != "2":
            print("Please type 1 or 2")
            continue
        else:
            break

choiceOfOneOrTwo(methodOfAbstraction)

if methodOfAbstraction == "1":
    leave = input("Leave the country?")
    if leave == "No":
        exit()
    else:
        transportation = input("Leave by car or bus?")
        if input == "Car":
            print("You drive to the port by car")
        else:
            print("You go to the port by bus")

    print("You take the boat to the other country")
    print("You are driven to the refugee camp")
    exit()

elif methodOfAbstraction == "2":
    leave = input("Leave the country? 1 for yes. 2 for no.")
    choiceOfOneOrTwo(leave)
    if leave == "1":
        transportation = input("Leave by car or bus. 1 for car. 2 for bus.")
        choiceOfOneOrTwo(transportation)
        if transportation == "1":
            print ("You arrive at the port by car and get on the boat")
        else:
            print ("You arrive the port by bus and get on the boat")
death = random.randint(1,2)
if death == 1:
    print("You die on the boat of starvation.")
else:
    input("You survive and get to the other country")
    print("You are driven to the refugee camp")
    exit()


