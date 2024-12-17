# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


print("Welcome to Johni's Auction Project!!!")
print("Lets start the bids")



Continue = True
aduction= {}


while Continue:

    Name = input("What is your name?".lower())
    Bid = int(input("what is your bid? $"))
    aduction[Name] = Bid

    cont = input("Is there anyone else who wants to make a bid?").lower()

    if cont == "yes":
        print("\n" * 20)
        Continue = True
    else :
        print("That will conclude the bids")
        Winner = ""
        MaxBid = 0

        for key in aduction:
            #print(key)
            #print(aduction[key])
            if aduction[key] > MaxBid:
                Winner = key
                MaxBid = aduction[key]
        print("\n" * 20)
        print(f"The Winner of today's Bid is {Winner} who had a bid of ${MaxBid}")
        Continue = False

print("Thanks for attending Johni's Aduction please leave.")


