# Base class 1:
class Father:
    fathername = "Apple"
    fatherage = 58

    def fathername(self):
        print(self.fathername)

    def changeFatherAge(self, a):
        self.fatherage = a

# Base class2:


class Mother:
    mothername = "Orange"
    age = 48

    def mothername(self):
        print(self.mothername)

# derived class or sub class


class Son(Father, Mother):
    def parents(self):
        print("Father:", self.fathername)
        print("Mother:", self.mothername)


obj1 = Son()
obj1.fathername = "Natarajan"
obj1.mothername = "Jamuna"
obj1.changeFatherAge(60)
print(obj1.fatherage)
obj1.parents()
