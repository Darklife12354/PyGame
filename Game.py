import random

while True:
    print("Lets play a game...")
    num1 = random.randint(1, 500)
    num2 = random.randint(1, 500)
    print("What is " + str(num1) + " + " + str(num2) + "?")
    answer = input("Your Answer : ")
    if answer.isdigit():
        if int(answer) == num1 + num2:
            print("Correct! The answer is " + str(num1 + num2) + "!")
            con = input("Do you wish to continue? (Yes or No) : ")
            if con == "Yes":
                print("Ok trying again!")
                continue
            elif con == "No":
                print("Ok closing...")
                quit()
        else:
            print("Wrong ! The correct answer is " + str(num1 + num2) + "!")
            con = input("Do you wish to continue? (Yes or No) : ")
            if con == "Yes":
                print("Ok trying again!")
                continue
            elif con == "No":
                print("Ok closing...")
                quit()
    else:
        print("Please use numbers next time !")
        con = input("Do you wish to continue? (Yes or No) : ")
        if con == "Yes":
            print("Ok trying again!")
            continue
        elif con == "No":
            print("Ok closing...")
            quit()
