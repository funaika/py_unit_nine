class Dog:
    def __init__(self, name):
        self.name = name
        self.trickList = []

    def getName(self):
        return self.name

    def do_trick(self, trick):
        self.trickList.append(trick)

    def print_tricks(self):
        if not self.trickList:
            print(self.name, "has not performed any tricks yet.")
        else:
            print(self.name, "has performed the following tricks:")
            for trick in self.trickList:
                print(trick)
    def sit(self):
        print(self.name, "sits")
        self.trickList.append("sit")

    def layDown(self):
        print(self.name, "lays down")
        self.trickList.append("lay down")

    def rollOver(self):
        print(self.name, "rolls over")
        self.trickList.append("roll over")

    def printTrickList(self):
        if not self.trickList:
            print(self.name, "has not performed any tricks yet.")
        else:
            print(self.name, "has performed the following tricks:")
            for trick in self.trickList:
                print(trick)

'''
dog1 = Dog("Spot")
dog1.sit()
dog1.rollOver()
dog1.printTrickList()

dog2 = Dog("Peanut")
dog2.sit()
dog2.layDown()
dog2.printTrickList()
'''