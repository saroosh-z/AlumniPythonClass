'''s = 'PythonClass'

count = 0
for i in s:
    count += 1
print(f'length of the string is: {count}')
'''
#num = int(input("Enter a number: "))

# Python program to check if the input number is prime or not
def prime_number(num):
    # take input from the user
    #num = int(input("Enter a number: "))

# prime numbers are greater than 1
    if num > 1:
# check for factors
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num) # The two back slashes seem to produce an interger
                break
            else:
                print(num,"is a prime number")

# if input number is less than
# or equal to 1, it is not prime
    else:
        print(num,"is not a prime number!")
prime_number(9)
