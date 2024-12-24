import random

def Sum(list):
    Sum =0
    for x in list:
        Sum = Sum + x
    return Sum


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
UserCards =[]
DealerCards = []

#start = input("Do you want to play a game of Black Jack? Type 'y' or 'n': ")

UserCards.append(cards[random.randint(0, 12)])
UserCards.append(cards[random.randint(0, 12)])

Score = Sum(UserCards)

print(f"Your cards: {UserCards}, Current Score: {Score}")

# Dealers Card

DealerCards.append(cards[random.randint(0, 12)])
DealerCards.append(cards[random.randint(0, 12)])
print(f"Computer 1st card: {DealerCards[0]}")
#print(DealerCards)


#TODO Ask if user wants another card and calc score
Cont = True
while Cont:

    Hit = input("Type 'y' to get another card, type 'n' to pass: ")

    if Hit == 'y':
        UserCards.append(cards[random.randint(0, 12)])
        Score = Sum(UserCards)


        # TODO Check to see if user pass 21
        if Score > 21:

            # TODO If you pass 21 but you have an 11 we convert to 1 and reScore
            if 11 in UserCards:
                UserCards[UserCards.index(11)] = 1
                Score = Sum(UserCards)

                #TODO IF user still has more than 21 you lose
                if Score > 21:
                    print(f"Your cards: {UserCards}, Current Score: {Score} You Lose!!!!!")
                    Cont = False

                print(f"Your cards: {UserCards}, Current Score: {Score}")
                Cont = True

            Cont = False
            print(f"Your cards: {UserCards}, Current Score: {Score} You Lose!!!!!")
            DScore = Sum(DealerCards)
            print(f"Computer Final Hand: {DealerCards}, Final Score{DScore}")

        # TODO User Did not pass 21 and can still ask for more cards
        else:

            print(f"Your cards: {UserCards}, Current Score: {Score}")
            Cont = True


    # TODO User decides not to take another cards
    else:
        DScore = Sum(DealerCards)
        print(f"Your cards: {UserCards}, Current Score: {Score}")

        while DScore < 17:
            DealerCards.append(cards[random.randint(0, 12)])
            DScore = Sum(DealerCards)
            print(DealerCards)

        if DScore < Score:

            print(f"Computer Final Hand: {DealerCards}, Final Score{DScore} You Win!!!!!!!!!")
            Cont = False
        else:
            print(f"Computer Final Hand: {DealerCards}, Final Score{DScore} You Lose!!!!!!!!!")
            Cont = False




