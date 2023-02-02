class Employee:
    name = "daniel"
    address = "pondy"

    # # constructor
    # def __init__(self):
    #     # self.name = name
    #     # self.age = age
    #     print("init method is invoked")


obj1 = Employee()
obj2 = Employee()

obj1 = obj2

print(obj1)
print(obj2)

print(obj1 is obj2)

# obj1.name = "xxx"
# obj1.address = "yyy"

# print(obj1.name)
# print(obj1.address)

print()

# print(Employee.name)
# print(Employee.address)
