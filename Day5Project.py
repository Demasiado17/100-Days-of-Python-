from random import randint

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(len(letters))
print(len(numbers))
print(len(symbols))




print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letlen= len(letters) -1

numlen= len(numbers) -1
symlen= len(symbols) -1

password =""

#randL= randint(0,letlen)
#print(randL)
#randN= randint(0,numlen)
#print(randN)
#randS= randint(0,symlen)
#print(randS)


for x in range(nr_letters):
    randL = randint(0, letlen)

    password = password + letters[randL]

    print(password)


for x in range(nr_symbols):
    randS = randint(0, symlen)
    password = password + symbols[randS]
    print(password)


for x in range(nr_numbers):
    randN = randint(0, numlen)
    password = password + numbers[randN]
    print(password)

print("final password" + password)

l = len(password)

print(l)



nPass = []
check = []

for i in range(0,l):

    #pick random number put into R
    R= randint(0,l-1)

    if R  not in check:
        print("New Random Number")
        nPass.append(password[R])
        check.append(R)
        print(check)
        print(nPass)

    else:
        print("Rerolling random num")
        R = randint(0, l - 1)
        if R not in check:
            print("New Random Number")
            nPass.append(password[R])
            check.append(R)
            print(check)
            print(nPass)

        else:
            print("Rerolling random num")
            R = randint(0, l - 1)
            if R not in check:
                print("New Random Number")
                nPass.append(password[R])
                check.append(R)
                print(check)
                print(nPass)
            else:


                print("already used")
                print(check)
                print(nPass)


print(f"New New Password is:{nPass}")



#for i in range(0,l):