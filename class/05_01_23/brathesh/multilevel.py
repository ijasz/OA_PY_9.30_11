# bass Class
class King:
    def __init__(self, kingName):
        self.kingName = kingName

# Derived Class1:


class Queen(King):
    def __init__(self, queenName):
        self.queenName = queenName

# Derived Class2:


class Prince (Queen):
    def __init__(self, princeName, queenName, kingName):
        # King.__init__(self, kingName)
        Queen.__init__(self, queenName)
        self.princeName = princeName

    def names(self):
        # print("King Name: ", self.kingName)
        print("Queen Name: ", self.queenName)
        print("Prince Name: ", self.princeName)


# code
obj1 = Prince("Jack", "Veronica", "Addams")
obj1.names()
