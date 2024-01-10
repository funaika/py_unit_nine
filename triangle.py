class Triangle:
    def __init__(self, sideOne, sideTwo, sideThree):
        self.sideOne = sideOne
        self.sideTwo = sideTwo
        self.sideThree = sideThree

    def calcPerimeter(self):
        return self.sideOne + self.sideTwo + self.sideThree

    def calcArea(self):
        perimeter = self.calcPerimeter()
        s = perimeter / 2
        area = (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
        return area