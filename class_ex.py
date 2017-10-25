class Parent:
  def test(self):
      print('You are in the parent class')

class Child(Parent):
    def test(self):
        print('this function is for child class. it\'s mine')
        super().test()


dad = Parent()
dad.test()

son = Child()
son.test()
