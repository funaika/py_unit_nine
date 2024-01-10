class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculatePerimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter

    def calculateArea(self):
        area = self.width * self.height
        return area