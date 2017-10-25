'''### List Functions
#To Create an empty List
my_list = []

# to create a list with elements
my_list = ['l','e','t','t','e','r','s', 'with', 'there']
print(f"original list {my_list}")
my_list.remove('th')
print(f'list after removing th: {my_list}')
#to get the length of a List
list_size = len(my_list)
print(f'my_list\'s size is: {list_size}')


#to access a particular element from the list
#accessing element at index 2
my_list[2]
my_list[1]
my_list[0]
#my_list[9]

#to add a single element to a list_size
my_list.append('h')

## To add more than one element to a list
to_add = ['to', 'add', 'more', 'elements']
my_list.extend(to_add)

#to get a list's slice
#to get elements from index 3 to 6
my_list[3:6]
#to access all the elements:
my_list[:]
#to access first 3 items
my_list[:3]
#to access last three items
print(f'last 3 items: {my_list[-3:]}')
##TO DO: read on accessing elements using negative index





print(f'accessing elements from index 3 to 6 {my_list[3:6]}')
print(f'last 3 elements {my_list[3:]}')
print(f'list before removing t: {my_list}')
#to remove an element or item from a list
my_list.remove('t')
print(f'list after removing t: {my_list}')

#to delete using an index
del my_list[3]
#to return an element and then delete it
deleted_element = my_list.pop(7)

#to empty out a list
my_list.clear()
#to sort a list
my_list.sort()
#to reverse elements' order in the list
my_list.reverse()'''
##################DICTIONARY########################
'''print("Dictionaries start here")
d = dict()
d['name'] = 'saroosh'
d['gender'] = 'f'
d['City'] = 'Yonkers'
d['state'] = 'NY'

print(d)
#print(d[0])
print(d['state'])

#s = 'purpleBanana'''
#count = dict()

'''create a dictionary
add 3 key-value pairs to it
write a loop to iterate over the dictionary and print out each key, value pair
check if a given value is in the dictionary or not
'''
'''for i in s:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(f"string {s} has the following count: \n {count}")

'''

###create a dictionary
d2 = dict()
d2['name'] = 'saroosh'
d2['gender'] = 'f'
d2['City'] = 'Yonkers'
d2['state'] = 'NY'
print(d2)
d2['City'] = 'the bronx'
print(d2)


#string = input('>>')
'''for s in d2:
    if string == d2[s]:
        print('yes')

string = input('enter a string::') #banana'
## step1 : initalize an empty dictionary
d = dict()
## step2 : a for loop to iterate through the string:
for letter in string:
    if letter in d:
        d[letter] += 1
    else:
        d[letter] = 1

print(d)
'''
