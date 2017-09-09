average1 = (45+55+65)/3
#print (f"average for 3 numbers is {average1}")

average2 = (55+65+98+12+15)/5
#print(f"average for 5 numbers is {average2}")

##########################
# using .format
message = "The average for {} numbers is {}"
print(message.format(3, average1))
print(message.format(5,average2))
