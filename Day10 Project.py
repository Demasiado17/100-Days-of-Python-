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

Keys = {"+" : add(a,b),
        "-" : sub(a,b),
        "*" : multi(a,b),
        "/" : divide(a,b) }


#TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
result =Keys[op]

print(f"The results of {a} {op} {b} is {result}")


Continue = True

while Continue:
    
    cont = input(" Continue? y for Yes , n for No").lower
