'''##create a dictionary

d = dict()
#d[city] = state
##7 elements
l = []
l['key'] = 1


d['NYC'] = 'New York'
d['Queens'] = 'New York'
d['Brooklyn'] = 'New York'
d['Philly'] = 'PA'
print(d)
''''''
for i in d:
    print(i), print(d[i])
    print(f'{i}: {d[i]}')''''''
##only print PA. KEy is Philly
print(d['Philly'])'''


'''s = "this is a sample string"
l = s.split('i')
print(s.split())
print(len(l))'''
'''###Read a file####
filename  = open('test.txt', 'r')
#print(filename)
r = filename.read(3)
#print(r)
filename  = open('file.txt', 'a')
filename.write(r)
'''
x = 10
def add():
    global x
    y = 9
    result = x + y
    x = result
    print(result)
    print(x)

add()
