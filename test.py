def triangle_check():
#First we assigned variables to make it easy
    a = int(input("What is your first length\n > "))
    b = int(input("\nWhat is your second length?\n > "))
    c = int(input("\nWhat is your final length?\n > "))
#We made conditionals
    if a > (a + b or b + c or a + c):
        print("This is not a triangle")
    elif b > (a + b or b + c or a + c):
        print("This is not a triangle")
    elif c > (a + b or b + c or a + c):
        print("This is not a triangle")
#Since we already have what will not give us triangle
    else:
#We made an else..  cause we're lazy
        print("This is a triangle")

triangle_check()
