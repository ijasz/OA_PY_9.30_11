class Sports:
    def __init__(self, sportsName, playerName):
        self.sportsName = sportsName
        self.playerName = playerName

    def play(self):
        print(f"{self.playerName} is playing {self.sportsName}")


obj1 = Sports("cricket", "dhoni")

print(obj1.sportsName, obj1.playerName)
obj1.play()
