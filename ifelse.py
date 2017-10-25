from sys import argv
#script = argv
#n = int (argv[1])
n = int(input('>>'))

print(n)
if (n >= 0):
    print("the number you entered is positive")
elif (n <0):
    print("the number you entered is negative")
else:
    print("you did not enter a number ")

###############functions and conditions #################

def print_one():
    print("this is a call to function print_one")
def print_two():
    print("this is a call to print_two")
def activity(a, b):
    if (a > b):
        print (a / b)
        print_one()
    elif(b > a):
        c = a * 10
        print_two()
    else:
        print("both are the same")

activity(8, 9)
