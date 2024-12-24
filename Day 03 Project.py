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






######################################################################################################################
######################################################################################################################

######################################################################################################################
######################################################################################################################

######################################################################################################################
######################################################################################################################

########################################## Demasiado Day 3 ###########################################################




print(r'''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first = input("Right Or Left? \nEnter 1 for Right and 0 for Left\n")

if first == "1":
    print (" you walked into a room with no light, can't see anything.\n"
           " You tripped down some stairs and broke your neck.\n"
           " You died and your quest is over now!\n RIP like the Yankees WS 2024")
    print(r'''
                ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#''')
else:
    print("You walked into a room with lights and was able to identify two more paths.\n"
          "One of the path has Green lights a calming aura coming from it.\n"
          "while the other path is dark and smells pretty bad. you think its pee mixed with blood \n")


    second=input("Which path are you taking. Light or Dark.\nEnter 1 for Light and 0 for Dark\n")

    if second == "1":
        print("At least we know you have common sense XD.\n"
              "Anyways you walked the path nothing bad happens to you.\n"
              "You see a door at the end of the path.\n "
              "you got closer and notcie a big Trump 2024 sign on the front of the door.\n"
              "Its not too late to turn around and take the Dark path.\n"
              "you only been walking for about 45 mins down this path. \n")


        third= input ( "Open the door Or Turn Around?\nEnter 1 for open door and 0 for Turn Around \n")


        if third == "0":
            print ("that way the right choice to make.\n"
                   "Never purposely walk into a Room with a Trump 2024 Sign on it.\n"
                   "For all you know it could of been a Diddy party.\n"
                   "Nevertheless as you turned around the door opened anyways!!\n"
                   "But to your surprise it was ChrisTREY that greeted you.\n"
                   "He explained that the door was a test and those truly worthy,\n"
                   "would never attempt to open the door.\n"
                   "In fact the moment you would of touched the doorknob. you would of died from posion.\n"
                   "ChrisTREY then tells you to come inside there's maaad talents in here.\n"
                   "Like any sane person you rush in immediately and grab 2 honey packs out your pocket\n"
                   "When you walked in you see some mid shorties sitting around smoking hookah.\n"
                   "But you also see 3 color doors aswell, you asked ChrisTrey about the doors.\n"
                   "He said that each room had a talent inside.\n"
                   "Without hesitation you decided to go in one of the doors off the honey.\n"
                   "Left door is Red, Middle door is blue, Right door is green.\n")

            fourth = input("Which door do you choose? Enter 1 for Red, 2 for Blue , 3 for Green\n")

            if fourth =="1":
                print("red door")

            elif fourth == "2":
                print("blue door")

            else:
                print("green door")





        else:
            print ("You decided to open the door which a huge grin on your face\n"
                   "however the moment you touched the doorknob\n"
                   "you fell down and died of posion. game over!!")

            print(r'''
            
     _.--""--._
    /  _    _  \
 _  ( (_\  /_) )  _
{ \._\   /\   /_./ }
/_"=-.}______{.-="_\
 _  _.=("""")=._  _
(_'"_.-"`~~`"-._"'_)
 {_"            "_}
            
            ''')






    else:
        print(" Are you stupid?? anyways you walked down this dark ass path, can barely see anything.\n"
              "After 7 mins of walking you start to wonder if you been going stright the whole 7 mins\n"
              "you then start to doubt if taking this path was the right choice.\n"
              "you turned around, but as soon as you did Deebo from Friday knocked you out and take your chain. \n"
              "You woke up with a black eye and a missing chain.\n"
              "Your journey ends here, lay there and reflect on your poor choices.\n")
        print(r'''
       ___             ___
      //  \           //  \
     //    )         //    )
     ||  _/          ||  _/                   __
     ||  \\_,&__     ||  \\                  (  \
     )|   ^  /  ``---,_\_/ &                 _>  )
     \|___,__\__       `\_  \_              (   /
                \__,-,    `\__\_             >_/
                     \_    /    `\_         / /
                       \_ /        \__    _/ /
                         `\          `\_,/  /
                     _     \__,-,  `   (_  /
                  __( \        ,)__   _/ \/
                 /     `-,___,-'   \_(  O `\
                 \     /_|___   ____/ \  \ =}
                  `---'      `-'       \_=_/{}
                                      .{}{}{}{.
                                      {}{}{}{}{
                                      }{}{}{}{}
                                      `}{}{}{}'
                                       `}{}{}           ''')










