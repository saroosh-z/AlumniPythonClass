'''s = 'purplebanana'

i = 0
while (i < len(s)):
    print(s[i])
    i = i+1

#7
filename = open('test.txt')
r = filename.readline()
print(len(r))

#8
def checkfl():
    s2 = 'banana'
    print(s2)
    for i in range(len(s2)):
        if s2[0] == s2[-1]:
            print('True')
            return True
        else:
            print('false')
            return False
checkfl()

#9
s3= 'parrot'
def key_lookup(s3, r):
    i = 0
    if 'r' in s3:
        print('yes')

key = key_lookup(s3, r)
print(key)

#10
t = [1,2,3,5]
def middle(t):
    return t[1:-1]

print(middle(t))


#5: Write a function that takes a letter and a string and returns True if the letter is in the given string, returns False otherwise

def charLookup(s, 'a'):

charLookup('hello', 'l')
'''

t = [1,2,3,5]
j = 0

def cumsum(t):
    print(f'original list: {t}')
    count = 0
    for i in range(len(t)):
        count += t[i]
        print (f'i: {i}. t[i]: {t[i]}, count: {count}')
        t[i] = count
    print(f'new list: {t}')

cumsum(t)
