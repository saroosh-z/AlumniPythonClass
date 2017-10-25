''class Math:
    def __init__(self,x, y):
        self.x = x
        self.y = y
    def add(self):
        return (self.x + self.y)
    def subtract(self): # x - y
        return (self.x - self.y)

class Math2(Math):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 5

    def multiply(self):
        return (self.x * self.y)
    def divide(self): # x / y
        a = (self.x / self.y)
        return a

        return self.x / self.y
#a = divide()
num1 = Math(4,5)
print(num1.add())

num2 = Math2(4,5)
print(num2.multiply())

class Math3:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = Math2(x,y).z
        self.sum = Math(x,y).add()
        self.mul = Math2(x,y).multiply()
    def stuff(self):
        print(f'z {self.z}')
    def exponent(self):
        return (self.x ** self.y)
    def add(self):
        return (self.add)
    def multiply(self):
        return (self.mul)

num3 = Math3(2,5)
print(num3.exponent())
print(f'num3 add: {num3.add()}')

print(num3.add())
print(num3.stuff())
###############################################
#######  EXAMPLE 2 ###########################
'''
class Increment:
    def __init__(self, x):
        self.num = x
    def inc (self):
        return (self.num+1)

inc  = Increment(5)
print(inc.inc())

class Decrement:
    def __init__(self, x):
        self.num = x
    def dec(self):
        return (self.num - 1)

dec = Decrement(5)
print(dec.dec())

class Timer:
    def __init__(self, x):
        self.num = x
        self.dec = Decrement(x)
        self.inc = Increment(x)
    def info(self):
        print(self.num)
        print(self.dec.dec())
        print(self.inc.inc())
t = Timer(5)
t.info()
'''
''
