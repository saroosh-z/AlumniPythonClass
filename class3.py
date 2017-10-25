class Employee:
    def __init__(self, f, l):
        self.firstName = f
        self.lastName = l

    def name(self):
        print(f'the person is: {self.firstName} {self.lastName}')

class Department(Employee):
    def __init__(self,f, l, d):
        Employee.__init__(self, f, l)
        self.department = d
    def name(self):
        print(f"the person is: {self.firstName} {self.lastName} from {self.department}")








p = Employee('saroosh', 'zaman')
p.name()
p2  = Employee('fname', 'lname')
p3 = Department('j', 'm','hr')
p3.name()
