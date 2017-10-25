


'''
for i in range(0, 10):
    print(i)
'''
'''for i in range(10):
    print(i)



for i in range(0, 10, 2):
    print(i)

i = 0
print('running while loop')
while (i < 5):
    print(i)
    i = i + 1

my_list = [1,2,3,4,5]
print(my_list)
'''
## 5 to 15
'''for x in range(12, 30, 2):
    #print('inside the for loop')
    print(x)
'''
'''word = 'Python class'
for letter in word:
    #print(letter)
    print("hello")
'''
'''i = 2
while (i == 2):
    print(i)
'''
'''numbers = []
print (numbers)
for i in range(1, 11):
    numbers.append(i)

print(numbers)
print(len(numbers))
print(numbers[4])'''

'''
for i in range(len(numbers)):
    print(numbers[i])

for i in numbers:
    print(i)
'''
#1. create a list that contains multiples of 2 from
    #12 to 48(including 48)


list_of_2s = []
print(list_of_2s) #it should be empty
for i in range(1, 13):
    list_of_2s.append(i)
    print(list_of_2s)
    print('hello')

list1 = [1,3,3,6,7,11,0,5]

print(f'sorted list1: {sort(list1)}')
list2 = [4,5,6]
list3 = list1+ list2
print(f'list3 is: {list3}')
#following code prints list elements 0, 1, 2
print(f'{list3[0:2]}')
#following code prints list elements 3, 4, 5
print(f'{list3[2:5]}')


for i in range(0, 3):
    list3.append(list1[i] + list2[i])

print(list3)


#print(list_of_2s)#it should be populated
