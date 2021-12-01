'''

    shapes.py

    Author: Daniel Lagesse
    Date: 2021-12-01

    Python Turtle shapes

'''
import turtle

class Polygon:
  def __init__(self, sides, name, size, color, line_thickness):
    self.sides = sides
    self.name = name
    self.size = size
    self.color = color
    self.line_thicness = line_thickness
    self.interior_angles = (self.sides - 2) * 180
    self.angle = self.interior_angles / self.sides

  def draw(self):
    for i in range(self.sides):
      turtle.forward(100)
      turtle.right(180 - self.angle)

class Triangle(Polygon):
  def __init__(self, size=100, color="black", line_thickness=3):
    super().__init__(3, "Triangle", size, color, line_thickness)

  def draw(self):
    turtle.begin_fill()
    super().draw()
    turtle.end_fill()

class Square(Polygon):
  def __init__(self, size=100, color="black", line_thickness=3):
    super().__init__(4, "Square", size, color, line_thickness)

  def draw(self):
    turtle.begin_fill()
    super().draw()
    turtle.end_fill()

class Pentagon(Polygon):
  def __init__(self, size=100, color="black", line_thickness=3):
    super().__init__(5, "Pentagon", size, color, line_thickness)

  def draw(self):
    turtle.begin_fill()
    super().draw()
    turtle.end_fill()

class Hexagon(Polygon):
  def __init__(self, size=100, color="black", line_thickness=3):
    super().__init__(6, "Hexagon", size, color, line_thickness)

  def draw(self):
    turtle.begin_fill()
    super().draw()
    turtle.end_fill()

class Octagon(Polygon):
  def __init__(self, size=100, color="black", line_thickness=3):
    super().__init__(8, "Octagon", size, color, line_thickness)

  def draw(self):
    turtle.begin_fill()
    super().draw()
    turtle.end_fill()

if __name__ == "__main__":
  triangle = Triangle()
  square = Square()
  pentagon = Pentagon()
  hexagon = Hexagon()
  octagon = Octagon()

  triangle.draw()

  turtle.done()