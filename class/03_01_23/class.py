# class Schools:
#     def __init__(self, schoolName, schoolAddress, schoolRank):
#         self.schoolName = schoolName
#         self.schoolAddress = schoolAddress
#         self.schoolRank = schoolRank

#     def location(self):
#         print(f"{self.schoolName} is located at {self.schoolAddress}")

#     def rank(self):
#         print(f"{self.schoolName} is ranked {self.schoolRank}")


# obj1 = Schools("Cluny", "Lawspet", 1)
# obj2 = Schools("Petit", "Uppalam", 20)
# obj1.location()
# obj1.rank()
# obj2.location()
# obj2.rank()

# SINGLE INHERITANCE

#  Base class => Parent class
class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def fullName(self):
        print(self.firstName + " " + self.lastName)


# Derived class => Child class
class Student(Person):
    rollnumber = 13423


obj1 = Student("Ramesh", "Vasanth")
obj1.fullName()
print(obj1.firstName)
print(obj1.lastName)
print(obj1.rollnumber)
