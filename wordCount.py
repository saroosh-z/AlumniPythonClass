#open a file
def line_count():
    file_to_count = open('test.txt')
    print(file_to_count)
    count = 0
    for line in file_to_count:
        count += 1
    print(count)
    return count

line_count()

#### see if a string has letters a, e, i, - return yes or no

s = input(>>) helloWorld
if e in s:
    print(f'{a}: yes')
    return True
