#TODO: Write out the other 3 functions - subtract, multiply and divide.

a = int(input("First number?"))
op = input("What mathematical operator? choices: + , - , * or / ")
b = int(input("Second number?"))

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

Keys = {"+" : add,
        "-" : sub,
        "*" : multi,
        "/" : divide }


#TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
result =Keys[op](a,b)

print(f"The results of {a} {op} {b} is {result}")


Continue = True

while Continue:

    x = input(" Continue with this result? y for Yes , n for No, any other input to exit.")

    if x == "y":
       a = result
       op = input("What mathematical operator? choices: + , - , * or / ")
       b = int(input("Second number?"))

       result = Keys[op](a,b)
       print(f"The results of {a} {op} {b} is {result}")
       Continue = True


    elif x == "n":
        print("\n" * 20)
        a = int(input("First number?"))
        op = input("What mathematical operator? choices: + , - , * or / ")
        b = int(input("Second number?"))


        result = Keys[op](a,b)
        print(f"The results of {a} {op} {b} is {result}")
        Continue = True

    else:
        print(x)
        Continue = False
