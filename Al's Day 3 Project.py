from turtledemo.chaos import jumpto

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
name: str = input("What is your name?")

#beginning
print("Welcome To My Saturday Night")
print(f"{name} walked into the club feeling lucky tonight. Should you go to the bar or bathroom?")
choice = input(" 1 for bar and 2 for bathroom ")


# First choice
if choice =="1":
    print(f"{name} went to the bar and meet a girl. \n Should you order a drink or speak to the girl?")
    choice_one = input("1 to order a drink and 2 to speak to the girl")

    if choice_one == "2":
        print(f"{name} Speaks with the girl.")

    # Second choice

        choice_two = input(f"{name} wants to ask her to dance.\n 1 to ask to dance 2 to say nothing: ")
        if choice_two == "1":
                print(f"{name} starts dancing with her now")



        # Third choice (only if choice_two is "1")

                choice_three = input(f"{name} Danced a beautiful bachata and want\'s to continue the night with her. \n 1 go for a kiss,2 do nothing, 3 grab a drink")
                if choice_three == "1":
                    print(f"{name} Goes for the kiss and she enjoyed every minute of it")

                    #Forth choice

                    choice_four = input(f"{name} kissed her and wanted to see if she wanted to continue the night. \n  1 ask her to go back to your place ,2 do nothing, 3 go to the bathroom, 4 try your luck with someone else")
                    if choice_four== "1":
                        print("She decided to go back to your place! \n Congrats you win!")
                    elif choice_four == "2":
                        print(" Because you didn't do anything she got bored and left. \n Game Over")
                    elif choice_four == "3":
                        print(f" You told her you needed to go to the bathroom real quick. Upon entering the bathroom you get robbed \n Game Over")
                    elif choice_four == "4":
                        print("You decided not to continue the night with her after seeing someone else. You say bye to her and go after the other person. \n You know what they say when the streets are calling.  \n Good Luck")
                    else:
                        print("Error Please try Again")




                elif choice_three == "2":
                    print("Because you didn't do anything, she got bored and left. \nGame Over.")

                elif choice_three == "3":
                    print(f"{name} got drinks with her, but it didn't sit well afterward. {name} went to the bathroom and got robbed. \nGame Over.")

                else:
                    print("Error: Please enter '1', '2', or '3'. Try again.")
                      # Exit loop after choice_three is handled
        elif choice_two == "2":
            print("Because you didn't say anything, another guy took her. \nGame Over.")

        else:
            print("Error: Please enter '1' or '2'. Try again.")

    # choice_one game over
    elif choice_one == "1":
        print(f"{name} got the drink and had to go throw up in the bathroom. \nUpon reaching the bathroom, he got robbed. \nGame Over.")
    else:
        print("Error: Please enter '1' or '2'. Try again.")

# first game over if user chose bathroom initially
elif choice == "2":
    print(f"{name} decided to go to the bathroom and got robbed. \nGame Over.")
else:
    print("Error: Please enter '1' or '2'. Try again.")


