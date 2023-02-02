class Parent:
    def par(self):
        print("This is Parent class")


class Child1(Parent):
    def func1(self):
        print("This is child 1 class")


class Child2(Parent):
    def func2(self):
        print("This is child 2 class")


class Combined(Child1, Child2):
    def func12(self):
        print("This is Combined class")


obj1 = Combined()
obj1.func12()
obj1.func2()
obj1.func1()
obj1.par()
